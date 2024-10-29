use std::collections::HashMap;
use std::net::TcpStream;
use std::io::{self, Read, Write};

pub struct NetworkClient {
    connections: HashMap<String, TcpStream>,
    timeout_ms: u64,
}

impl NetworkClient {
    pub fn new(timeout_ms: u64) -> Self {
        NetworkClient {
            connections: HashMap::new(),
            timeout_ms,
        }
    }

    pub fn process_request(&mut self, host: &str, data: &[u8]) -> io::Result<Vec<u8>> {
        let stream = match self.connections.get_mut(host) {
            Some(stream) => stream,
            None => {
                let stream = TcpStream::connect(host)?;
                stream.set_read_timeout(Some(std::time::Duration::from_millis(self.timeout_ms)))?;
                self.connections.insert(host.to_string(), stream);
                self.connections.get_mut(host).unwrap()
            }
        };

        stream.write_all(data)?;
        
        let mut response = Vec::new();
        stream.read_to_end(&mut response)?;
        Ok(response)
    }

    pub fn close_connection(&mut self, host: &str) -> io::Result<()> {
        if let Some(stream) = self.connections.remove(host) {
            drop(stream);
        }
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_connection_lifecycle() {
        let mut client = NetworkClient::new(5000);
        let result = client.process_request("localhost:8080", b"test data");
        assert!(result.is_err()); // Expected since no server is running
        
        client.close_connection("localhost:8080").unwrap();
    }
}