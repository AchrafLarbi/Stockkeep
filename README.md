StockKeep

StockKeep is a comprehensive web and mobile application designed to revolutionize the way you manage inventory. Its primary objective is to automate the entire inventory process, making stock management straightforward, efficient, and error-free. By leveraging advanced technology, StockKeep helps businesses track inventory levels with precision, streamline restocking processes, and prevent shortages that can disrupt operations. With real-time monitoring capabilities, StockKeep ensures that your inventory is always up-to-date, enabling smooth and uninterrupted business operations.
Table of Contents:

  Features
  
  Technologies Used
  
  Installation
  
  Usage

  Contact

Features:

  Real-Time Inventory Tracking: Monitor inventory levels in real-time to avoid stockouts and overstock situations.
  
  Automated Restocking Notifications: Receive alerts when inventory levels fall below predefined thresholds, ensuring timely restocking.
  
  Detailed Analytics and Reporting: Gain insights into inventory trends, sales data, and restocking patterns with comprehensive analytics and reports.
  
  User Authentication and Role Management: Secure user access with authentication and define roles for different user types (e.g., admin, service-achat, magasinier).
  
  Mobile-Friendly Interface: Access and manage your inventory from anywhere using the mobile-friendly application.  
  
  Supplier Management: Keep track of suppliers, manage purchase orders, and streamline the procurement process.
  
  Multi-Location Support: Manage inventory across multiple locations and warehouses seamlessly.
  
  Customizable Alerts: Set up custom alerts for various inventory events such as low stock, expiring products, and more.
  
  Audit Trail: Maintain a detailed log of all inventory transactions for accountability and auditing purposes.

Technologies Used:

  Backend: Python, Django, Django REST Framework
  Frontend: React, Tailwind CSS, Vite

Installation:
Backend Setup

  Clone the repository:


    git clone https://github.com/yourusername/stockkeep.git
    cd stockkeep

  Create and activate a virtual environment:

    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`

  Install the dependencies:



    pip install -r requirements.txt

  Run the migrations:

    python manage.py migrate

  Start the backend server:


    python manage.py runserver

Frontend Setup

  Navigate to the frontend directory:


    cd frontend

  Install the dependencies:


    npm install

  Start the frontend development server:

    npm run dev

Usage

    Open your browser and navigate to http://localhost:8000 to access the backend.
    Open your browser and navigate to http://localhost:3000 to access the frontend.

Contact

For questions or support, please contact us at Procodestockkeep@gmail.com.
