 This file consists of a file-based key-value data store that supports the basic CRD(create, read, write) operations. Data store is meant to be used as a local storage for one single process on single laptop.This data store is exposed as a library to clients that can instantiate a class and work with the data store.The data store will support some Functional and Non-functional Requirements.

Functional Requirements:
1) It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.
2) A new key-value pair can be added to the data store using the Create operation. The key is always a string-capped at 32chars.The value is always a JSON object-capped at 16KB.
3) If Create is invoked for an existing key, an appropriate error must be returned.
4) A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.
5) A Delete operation can be performed by providing the key.
6) Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds    the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
7) Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits.

Non-functional Requirements:
1) More than one client process cannot be allowed to use the same file as a data store at any given time.
2) A client process is allowed to access the data store using multiple threads,if it desires to.

Go through the attached operation.py file, maincode.py files that are attached here with in order to understand clearly how the code works and how to perform operations in this.
