#!/usr/bin/env python3

import argparse
import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, 
                     use_digits=True, use_symbols=True, no_similar=False):
    """Generate a random password with specified options"""
    
    # Define character sets
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    digit_chars = string.digits
    symbol_chars = string.punctuation
    
    # Remove similar characters if specified
    if no_similar:
        similar_chars = "Il1O0o"
        uppercase_chars = ''.join(c for c in uppercase_chars if c not in similar_chars)
        lowercase_chars = ''.join(c for c in lowercase_chars if c not in similar_chars)
        digit_chars = ''.join(c for c in digit_chars if c not in similar_chars)
    
    # Build character pool based on options
    char_pool = ""
    if use_uppercase:
        char_pool += uppercase_chars
    if use_lowercase:
        char_pool += lowercase_chars
    if use_digits:
        char_pool += digit_chars
    if use_symbols:
        char_pool += symbol_chars
    
    # Ensure at least one character type is selected
    if not char_pool:
        print("Error: At least one character type must be enabled")
        return None
    
    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password")
    
    parser.add_argument("-l", "--length", type=int, default=12, help="Password length (default: 12)")
    parser.add_argument("--no-upper", action="store_true", help="Don't include uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Don't include lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Don't include digits")
    parser.add_argument("--no-symbols", action="store_true", help="Don't include symbols")
    parser.add_argument("--no-similar", action="store_true", help="Don't include similar characters (Il1O0o)")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of passwords to generate (default: 1)")
    
    args = parser.parse_args()
    
    # Generate passwords
    for i in range(args.count):
        password = generate_password(
            length=args.length,
            use_uppercase=not args.no_upper,
            use_lowercase=not args.no_lower,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
            no_similar=args.no_similar
        )
        
        if password:
            if args.count > 1:
                print(f"Password #{i+1}: {password}")
            else:
                print(password)

if __name__ == "__main__":
    main()
