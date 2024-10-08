use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let nums:Vec<i8> = input
        .split_whitespace()
        .map(|s| s.parse::<i8>().unwrap())
        .collect();

    println!("{}", nums[0] - nums[1]);
}