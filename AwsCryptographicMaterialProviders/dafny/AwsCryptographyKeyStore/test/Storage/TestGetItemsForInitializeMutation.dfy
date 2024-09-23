// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../Fixtures.dfy"

module {:options "/functionSyntax:4"} TestGetItemsForInitializeMutation {
  import UInt = Fixtures.UInt
  import Types = Fixtures.Types
  import UTF8 = Fixtures.UTF8
  import opened Wrappers
  import DefaultKeyStorageInterface
  import Fixtures
  import Structure
  import DDB = Com.Amazonaws.Dynamodb
  import KMS = Com.Amazonaws.Kms
  import KeyStore

  const physicalName: DDB.Types.TableName := Fixtures.branchKeyStoreName
  const logicalName := Fixtures.logicalKeyStoreName
  // The Key Store will consider this mutation lock invalid
  // The Storage layer will not.
  const mLockedId := "test-get-items-for-initialize-mutation"

  method {:test} TestHappyCase()
  {
    var underTest :- expect Fixtures.DefaultStorage();
    var input := Types.GetItemsForInitializeMutationInput(
      Identifier := Fixtures.branchKeyId
    );
    var output :- expect underTest.GetItemsForInitializeMutation(input);
    expect
      output.activeItem.Type.ActiveHierarchicalSymmetricVersion?,
      "activeItem was not Active? 'type': " + output.activeItem.EncryptionContext[Structure.TYPE_FIELD];
    expect
      output.beaconItem.Type.ActiveHierarchicalSymmetricBeacon?,
      "beaconItem was not Beacon? 'type': " + output.beaconItem.EncryptionContext[Structure.TYPE_FIELD];
    expect
      output.mutationLock.None?,
      "MutationLock was not None. 'UUID': " + output.mutationLock.value.UUID;
  }

  method {:test} TestHappyCaseMLocked()
  {
    var underTest :- expect Fixtures.DefaultStorage();
    var input := Types.GetItemsForInitializeMutationInput(
      Identifier := mLockedId
    );
    var output :- expect underTest.GetItemsForInitializeMutation(input);

    expect
      output.activeItem.Type.ActiveHierarchicalSymmetricVersion?,
      "activeItem was not Active? 'type': " + output.activeItem.EncryptionContext[Structure.TYPE_FIELD];
    expect
      output.beaconItem.Type.ActiveHierarchicalSymmetricBeacon?,
      "beaconItem was not Beacon? 'type': " + output.beaconItem.EncryptionContext[Structure.TYPE_FIELD];
    expect
      output.mutationLock.Some?,
      "MutationLock was not Some.";
  }
}