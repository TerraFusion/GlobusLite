# GlobusLite
[![PyPI version](https://badge.fury.io/py/globuslite.svg)](https://badge.fury.io/py/globuslite)
## Introduction

GlobusLite provides a lightweight interface to the Globus SDK for transferring files between different storage systems. The main goal of globuslite is to provide the user an abstraction of the Globus API authentication flow and a simple way to transfer batches of files without having to worry about the underlying details of the SDK.

A common workflow looks like this:

```
import globuslite
globuslite.login()   # If not already logged in
transfer = globuslite.Transfer( 'd59900ef-6d04-11e5-ba46-22000b92c6ec', 
  'd59900ef-6d04-11e5-ba46-22000b92c6ec')

transfer.add_file( '/path/to/file1.txt', '/path/to/destination/file1.txt' )
transfer.add_file( '/path/to/file2.txt', '/path/to/destinatoin/fil2.txt' )

transfer.submit( label='Test Transfer', deadline='2018-05-05' )
```
