// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
package software.amazon.cryptography.keystore.model;

import java.util.Objects;

public class ClobberMutationLockInput {

  /**
   * Information an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  private final MutationLock MutationLock;

  protected ClobberMutationLockInput(BuilderImpl builder) {
    this.MutationLock = builder.MutationLock();
  }

  /**
   * @return Information an in-flight Mutation of a Branch Key.
   * This ensures:
   * - only one Mutation affects a Branch Key at a time
   * - all items of a Branch Key are mutated consistently
   */
  public MutationLock MutationLock() {
    return this.MutationLock;
  }

  public Builder toBuilder() {
    return new BuilderImpl(this);
  }

  public static Builder builder() {
    return new BuilderImpl();
  }

  public interface Builder {
    /**
     * @param MutationLock Information an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    Builder MutationLock(MutationLock MutationLock);

    /**
     * @return Information an in-flight Mutation of a Branch Key.
     * This ensures:
     * - only one Mutation affects a Branch Key at a time
     * - all items of a Branch Key are mutated consistently
     */
    MutationLock MutationLock();

    ClobberMutationLockInput build();
  }

  static class BuilderImpl implements Builder {

    protected MutationLock MutationLock;

    protected BuilderImpl() {}

    protected BuilderImpl(ClobberMutationLockInput model) {
      this.MutationLock = model.MutationLock();
    }

    public Builder MutationLock(MutationLock MutationLock) {
      this.MutationLock = MutationLock;
      return this;
    }

    public MutationLock MutationLock() {
      return this.MutationLock;
    }

    public ClobberMutationLockInput build() {
      if (Objects.isNull(this.MutationLock())) {
        throw new IllegalArgumentException(
          "Missing value for required field `MutationLock`"
        );
      }
      return new ClobberMutationLockInput(this);
    }
  }
}