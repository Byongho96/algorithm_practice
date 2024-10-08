use std::io;

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read input");

    let mut result = input
        .split_whitespace()
        .map(|s| s.parse::<u8>().unwrap())
        .sum::<u8>();
    
    println!("{}", result);
}
