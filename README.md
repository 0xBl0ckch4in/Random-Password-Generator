# 🔑 Random Password Generator

A simple command-line tool to generate secure random passwords.

## ✨ Features

- 🔐 Generate random passwords with customizable length
- 🔡 Control character types (uppercase, lowercase, digits, symbols)
- 👁️ Option to exclude similar-looking characters (Il1O0o)
- 🔢 Generate multiple passwords at once

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/password-generator.git
cd password-generator
```

2. Make the script executable (Unix/Linux/macOS):
```bash
chmod +x main.py
```

## 🔍 Usage

```bash
python main.py [options]
```

## ⚙️ Options

- `-l, --length`: Password length (default: 12)
- `--no-upper`: Don't include uppercase letters
- `--no-lower`: Don't include lowercase letters
- `--no-digits`: Don't include digits
- `--no-symbols`: Don't include symbols
- `--no-similar`: Don't include similar characters (Il1O0o)
- `-c, --count`: Number of passwords to generate (default: 1)

## 📝 Examples

### Generate a default password (12 characters with all character types):
```bash
python main.py
```

### Generate a longer password (16 characters):
```bash
python main.py -l 16
```

### Generate a PIN (digits only):
```bash
python main.py -l 6 --no-upper --no-lower --no-symbols
```

### Generate a password without symbols:
```bash
python main.py --no-symbols
```

### Generate a password without similar-looking characters:
```bash
python main.py --no-similar
```

### Generate multiple passwords:
```bash
python main.py -c 5
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.