// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
// Do not modify this file. This file is machine generated, and any changes to it will be overwritten.
#[allow(missing_docs)] // documentation missing in model
#[non_exhaustive]
#[derive(::std::clone::Clone, ::std::cmp::PartialEq, ::std::fmt::Debug)]
pub struct OnEncryptOutput {
    #[allow(missing_docs)] // documentation missing in model
pub materials: ::std::option::Option<crate::types::EncryptionMaterials>,
}
impl OnEncryptOutput {
    #[allow(missing_docs)] // documentation missing in model
pub fn materials(&self) -> &::std::option::Option<crate::types::EncryptionMaterials> {
    &self.materials
}
}
impl OnEncryptOutput {
    /// Creates a new builder-style object to manufacture [`OnEncryptOutput`](crate::types::OnEncryptOutput).
    pub fn builder() -> crate::types::builders::OnEncryptOutputBuilder {
        crate::types::builders::OnEncryptOutputBuilder::default()
    }
}

/// A builder for [`OnEncryptOutput`](crate::types::OnEncryptOutput).
#[non_exhaustive]
#[derive(
    ::std::clone::Clone, ::std::cmp::PartialEq, ::std::default::Default, ::std::fmt::Debug,
)]
pub struct OnEncryptOutputBuilder {
    pub(crate) materials: ::std::option::Option<crate::types::EncryptionMaterials>,
}
impl OnEncryptOutputBuilder {
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
    /// Consumes the builder and constructs a [`OnEncryptOutput`](crate::types::OnEncryptOutput).
    pub fn build(
        self,
    ) -> ::std::result::Result<
        crate::types::OnEncryptOutput,
        ::aws_smithy_types::error::operation::BuildError,
    > {
        ::std::result::Result::Ok(crate::types::OnEncryptOutput {
            materials: self.materials,
        })
    }
}
