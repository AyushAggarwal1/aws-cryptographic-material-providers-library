// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../../src/Index.dfy"
include "../../../AwsCryptographyKeyStore/test/CleanupItems.dfy"
include "../../../AwsCryptographyKeyStore/test/Fixtures.dfy"
include "../../../AwsCryptographyKeyStore/Model/AwsCryptographyKeyStoreTypes.dfy"
include "../AdminFixtures.dfy"

// Tests for T-28
// Assert the Pagination of results from storage grabs all Decrypt Only Versions
// This Test will:
// - Create a Branch Key and Version it 1 times
// - Initialize a Mutation of that Branch Key; one mutated version, two un-mutated version
// - Apply Mutation of that Branch Key with pageSize of 1
// - Assert:
// -- Apply returned Token with pageIndex
// -- There is a M-Lock
// ---- two mutated version, one un-mutated version
// - Apply Mutation of that Branch Key with pageSize of 1
// - Assert:
// -- Apply returned Complete
// -- There is no M-Lock
// -- All items have been mutated


module {:options "/functionSyntax:4" } TestThreat28 {
  import Types = AwsCryptographyKeyStoreAdminTypes
  import KeyStoreAdmin
  import KeyStore
  import KeyStoreTypes = AwsCryptographyKeyStoreTypes
  import opened Wrappers
  import Fixtures
  import AdminFixtures
  import UUID
  import CleanupItems
  import KMS = Com.Amazonaws.Kms
  import DDB = Com.Amazonaws.Dynamodb
  import DefaultKeyStorageInterface
  import Time
  import Structure
  import String = StandardLibrary.String
  import UTF8

  const happyCaseId := "test-apply-mutates-everything-before-completing"
  const customEC := "aws-crypto-ec:Robbie"
  const kmsId: string := Fixtures.keyArn
  const physicalName: string := Fixtures.branchKeyStoreName
  const logicalName: string := Fixtures.logicalKeyStoreName
  const testLogPrefix := "\nTestThreat28 :: TestHappyCase :: "

  method {:test} TestHappyCase()
  {
    print " running";

    var ddbClient :- expect Fixtures.ProvideDDBClient();
    var kmsClient :- expect Fixtures.ProvideKMSClient();
    var storage :- expect Fixtures.DefaultStorage(ddbClient?:=Some(ddbClient));
    var keyStore :- expect Fixtures.DefaultKeyStore(ddbClient?:=Some(ddbClient), kmsClient?:=Some(kmsClient));
    var strategy :- expect AdminFixtures.DefaultKeyManagerStrategy(kmsClient?:=Some(kmsClient));
    var underTest :- expect AdminFixtures.DefaultAdmin(ddbClient?:=Some(ddbClient));

    var uuid :- expect UUID.GenerateUUID();
    var testId := happyCaseId + "-" + uuid;

    Fixtures.CreateHappyCaseId(id:=testId, versionCount:=1);

    print testLogPrefix + " Created the test items with 2 versions! testId: " + testId + "\n";

    var activeOneInput := KeyStoreTypes.GetEncryptedActiveBranchKeyInput(Identifier:=testId);
    var activeOne? :- expect storage.GetEncryptedActiveBranchKey(activeOneInput);
    expect customEC in activeOne?.Item.EncryptionContext;
    expect activeOne?.Item.Type.ActiveHierarchicalSymmetricVersion?;
    var activeOne := activeOne?.Item.Type.ActiveHierarchicalSymmetricVersion.Version;
    var robbieOne := activeOne?.Item.EncryptionContext[customEC];

    print testLogPrefix + " Established ActiveOne: " + activeOne + "\n";

    var timestamp :- expect Time.GetCurrentTimeStamp();
    var newCustomEC: KeyStoreTypes.EncryptionContextString := map["Robbie" := timestamp];
    var mutationsRequest := Types.Mutations(TerminalEncryptionContext := Some(newCustomEC));
    var initInput := Types.InitializeMutationInput(
      Identifier := testId,
      Mutations := mutationsRequest,
      Strategy := Some(strategy));
    var initializeOutput :- expect underTest.InitializeMutation(initInput);
    var initializeToken := initializeOutput.MutationToken;

    expect initializeToken.UUID.Some?, "Mutation Token from InitializeMutation does not have a UUID!";

    print testLogPrefix + " Initialized Mutation. M-Lock UUID " + initializeToken.UUID.value + "\n";

    var testInput := Types.ApplyMutationInput(
      MutationToken := initializeToken,
      PageSize := Some(1), //Some(24),
      Strategy := Some(strategy));
    // var applyOutput :- expect underTest.ApplyMutation(testInput);
    var applyOutput? := underTest.ApplyMutation(testInput);
    if (applyOutput?.Failure?) {
      print applyOutput?;
    }
    expect applyOutput?.Success?, "Apply 1 FAILED";
    var applyOutput := applyOutput?.value;
    print testLogPrefix + " Applied Mutation w/ pageSize 1. testId: " + testId + "\n";
    expect applyOutput.MutationResult.ContinueMutation?, "Apply Mutation output should continue!";
    var applyToken: Types.MutationToken := applyOutput.MutationResult.ContinueMutation;
    expect applyToken.ExclusiveStartKey.Some?, "Apply Mutation output continues but pageIndex is None?";
    expect |applyToken.ExclusiveStartKey.value| > 0, "Apply Mutation output continues but pageIndex has length 0.";

    print testLogPrefix + " Apply 1 output met expectations. testId: " + testId + "\n";
    // TODO: Assert the M-Lock is still there
    // TODO: Assert log lines

    testInput := Types.ApplyMutationInput(
      MutationToken := applyToken,
      PageSize := Some(1),
      Strategy := Some(strategy));
    applyOutput? := underTest.ApplyMutation(testInput);
    if (applyOutput?.Failure?) {
      print applyOutput?;
    }
    expect applyOutput?.Success?, "Apply 2 FAILED";
    applyOutput := applyOutput?.value;

    // print testLogPrefix + " Applied 2 Mutation w/ pageSize 1. testId: " + testId + "\n";
    expect applyOutput.MutationResult.ContinueMutation?, "Apply Mutation output should continue, based on the DDB Limit";
    applyToken := applyOutput.MutationResult.ContinueMutation;
    expect applyToken.ExclusiveStartKey.Some?, "Apply Mutation output continues but pageIndex is None?";
    expect |applyToken.ExclusiveStartKey.value| > 0, "Apply Mutation output continues but pageIndex has length 0.";
    print testLogPrefix + " Apply 2 output met expectations. testId: " + testId + "\n";

    testInput := Types.ApplyMutationInput(
      MutationToken := applyToken,
      PageSize := Some(1),
      Strategy := Some(strategy));
    applyOutput? := underTest.ApplyMutation(testInput);
    if (applyOutput?.Failure?) {
      print applyOutput?;
    }
    expect applyOutput?.Success?, "Apply 3 FAILED";
    applyOutput := applyOutput?.value;
    expect applyOutput.MutationResult.CompleteMutation?, "Apply Mutation output should not continue!";

    var versionQuery := KeyStoreTypes.QueryForVersionsInput(
      Identifier := testId,
      PageSize := 24
    );
    var queryOut :- expect storage.QueryForVersions(versionQuery);
    var items := queryOut.Items;
    expect
      |items| == 3,
      "Test expects there to be 3 Decrypt Only items! Found: " + String.Base10Int2String(|items|);
    print testLogPrefix + " Read the 3 Decrypt Only items! testId: " + testId + "\n";

    var itemIndex := 0;
    var inputV: KeyStoreTypes.GetBranchKeyVersionInput;
    while itemIndex < |items|
    {
      var item := items[itemIndex];
      expect
        customEC in item.EncryptionContext,
                    "Robbie should be a Key in the Custom Encryption Context of all items for this test.";
      expect
        item.EncryptionContext[customEC] == timestamp,
        "Robbie's value should be the test timestamp for all decrypt items for this test.";
      expect "type" in item.EncryptionContext, "Decrypt Only item is missing 'type' from EC!!";
      expect
        item.Type.HierarchicalSymmetricVersion?,
        "Query for Decrypt Only returned a non-Decrypt Only!";
      var versionUUID := item.Type.HierarchicalSymmetricVersion.Version;
      inputV := KeyStoreTypes.GetBranchKeyVersionInput(
        branchKeyIdentifier := testId,
        branchKeyVersion := versionUUID
      );
      var _ :- expect keyStore.GetBranchKeyVersion(inputV);

      // This is a best effort
      var _ := CleanupItems.DeleteTypeWithFailure(testId, item.EncryptionContext["type"], ddbClient);
      print testLogPrefix + " Validated Decrypt Only and tried to clean it up: " + item.EncryptionContext["type"] + "\n";
      itemIndex := 1 + itemIndex;
    }
    print testLogPrefix + " Validated and tried to delete the read \"mutated\" test items! testId: " + testId + "\n";

    // Assert there is no M-Lock by running Initialize
    var initializeResult :=  underTest.InitializeMutation(initInput);
    expect initializeResult.Success?, "Apply 3 did not erase the Mutation Lock or Initialize Mutation is broken!";
    print testLogPrefix + " Apply 3 output met expectations. testId: " + testId + "\n";

    var lastActiveInput := KeyStoreTypes.GetEncryptedActiveBranchKeyInput(Identifier:=testId);
    var lastActive? :- expect storage.GetEncryptedActiveBranchKey(lastActiveInput);
    expect lastActive?.Item.Type.ActiveHierarchicalSymmetricVersion?;
    var lastActive := lastActive?.Item.Type.ActiveHierarchicalSymmetricVersion.Version;

    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BRANCH_KEY_ACTIVE_TYPE, ddbClient);
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BEACON_KEY_TYPE_VALUE, ddbClient);
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.MUTATION_LOCK_TYPE, ddbClient);
    var _ := CleanupItems.DeleteTypeWithFailure(testId, Structure.BRANCH_KEY_TYPE_PREFIX + lastActive, ddbClient);

    print "TestThreat28.TestHappyCase: ";
  }
}