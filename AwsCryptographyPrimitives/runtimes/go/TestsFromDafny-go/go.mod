module github.com/aws/aws-cryptographic-material-providers-library/primitives/test

go 1.23.0

replace github.com/aws/aws-cryptographic-material-providers-library/primitives v0.0.0 => ../ImplementationFromDafny-go

require github.com/dafny-lang/DafnyStandardLibGo v0.0.0

require (
	github.com/aws/aws-cryptographic-material-providers-library/primitives v0.0.0
	github.com/dafny-lang/DafnyRuntimeGo v0.0.0
)

replace github.com/dafny-lang/DafnyRuntimeGo => ../../../../smithy-dafny/DafnyRuntimeGo

replace github.com/dafny-lang/DafnyStandardLibGo => ../../../../StandardLibrary/runtimes/go/ImplementationFromDafny-go/