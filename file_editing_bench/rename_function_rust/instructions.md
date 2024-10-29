# Function Rename Task

In the file `network_utils.rs`, there is a method in the `NetworkClient` implementation called `proc` that processes network requests. This name is not descriptive enough.

Rename this method to `process_request` to better reflect its purpose of sending data to a host and receiving a response.

The function signature should change from:
```rust
pub fn proc(&mut self, host: &str, data: &[u8]) -> io::Result<Vec<u8>>
```

to:
```rust
pub fn process_request(&mut self, host: &str, data: &[u8]) -> io::Result<Vec<u8>>
```

Make sure to update all references to this function, including in the test module.