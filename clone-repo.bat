git clone https://github.com/BitDragon256/aoc2023.git
wget https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe
rustup-init.exe -y
cd aoc2023\src
rustc day01.rs
day01.exe >> correct.txt
exit