# Phase 3 Project: CLI

# Drink Order Management CLI

This is a Python CLI application for managing an order page for drinks. The application uses SQLAlchemy as the ORM to handle database operations and Click for the CLI interface. It allows users to create, delete, view, and find customers and orders.

## Features

- **Manage Customers**: Create, delete, list, and find customers.
- **Manage Orders**: Create, delete, list, and find orders.
- **Database**: Uses SQLite for storing customers and orders.
- **ORM**: SQLAlchemy is used for database operations.
- **CLI**: Click is used to create an interactive command-line interface.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python models.py
   ```

## Usage

Run the CLI application:
```bash
python app.py
```

### Commands

#### Drink Management
- `customer create`: Create a new customer.
- `customer delete`: Delete a customer by ID.
- `customer list`: List all customers.
- `customer find`: Find a customer by ID.

#### Order Management
- `order create`: Create a new order.
- `order delete`: Delete an order by ID.
- `order list`: List all orders.
- `order find`: Find an order by ID.

## Project Structure

```
.
├── app.py          # Main CLI application
├── models.py       # Database models and setup
├── requirements.txt # Dependencies
├── README.md       # Project documentation
```

## Dependencies

- Python 3.8
- SQLAlchemy
- Click

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.