// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(missing_docs)] // documentation missing in model
#[non_exhaustive]
#[derive(::std::clone::Clone, ::std::cmp::PartialEq, ::std::fmt::Debug)]
pub struct OnEncryptInput {
    #[allow(missing_docs)] // documentation missing in model
pub materials: ::std::option::Option<crate::types::EncryptionMaterials>,
}
impl OnEncryptInput {
    #[allow(missing_docs)] // documentation missing in model
pub fn materials(&self) -> &::std::option::Option<crate::types::EncryptionMaterials> {
    &self.materials
}
}
impl OnEncryptInput {
    /// Creates a new builder-style object to manufacture [`OnEncryptInput`](crate::types::OnEncryptInput).
    pub fn builder() -> crate::types::builders::OnEncryptInputBuilder {
        crate::types::builders::OnEncryptInputBuilder::default()
    }
}

/// A builder for [`OnEncryptInput`](crate::types::OnEncryptInput).
#[non_exhaustive]
#[derive(
    ::std::clone::Clone, ::std::cmp::PartialEq, ::std::default::Default, ::std::fmt::Debug,
)]
pub struct OnEncryptInputBuilder {
    pub(crate) materials: ::std::option::Option<crate::types::EncryptionMaterials>,
}
impl OnEncryptInputBuilder {
    #[allow(missing_docs)] // documentation missing in model
pub fn materials(mut self, input: impl ::std::convert::Into<crate::types::EncryptionMaterials>) -> Self {
    self.materials = ::std::option::Option::Some(input.into());
    self
}
#[allow(missing_docs)] // documentation missing in model
pub fn set_materials(mut self, input: ::std::option::Option<crate::types::EncryptionMaterials>) -> Self {
    self.materials = input;
    self
}
#[allow(missing_docs)] // documentation missing in model
pub fn get_materials(&self) -> &::std::option::Option<crate::types::EncryptionMaterials> {
    &self.materials
}
    /// Consumes the builder and constructs a [`OnEncryptInput`](crate::types::OnEncryptInput).
    pub fn build(
        self,
    ) -> ::std::result::Result<
        crate::types::OnEncryptInput,
        ::aws_smithy_types::error::operation::BuildError,
    > {
        ::std::result::Result::Ok(crate::types::OnEncryptInput {
            materials: self.materials,
        })
    }
}
