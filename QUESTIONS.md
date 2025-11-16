### 1. Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used and any other variable that you understand important on your development process.

I always like to modularize because it facilitates maintenance. Therefore, my strategy for implementing the application was to divide the project into frontend and backend, ensuring modularity and ease of maintenance.

Backend: I chose to use FastAPI with Python because it provides high performance, automatic API documentation, and ease of creating REST endpoints. I added CORS to allow requests from the frontend.

Frontend: I used React with hooks (useEffect and useState) to manage state and API calls. Choosing React allowed me to quickly create a responsive and reactive interface.

Complexity decisions: The application logic was kept simple, with data fetching via API and table rendering on the frontend.

Effort cost: I opted for modern and widely supported technologies (FastAPI, React, Docker) to reduce configuration and future maintenance effort. 

### 2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?

To add new columns in the future, I would proceed as follows:

Backend: Generally, the changes would affect the existing domains and some minor adjustments in the summary.

Frontend: Since I opted for a simpler approach, new columns would need to be added manually in the component. However, if a dynamic table approach were used, rendering columns based on the received data and avoiding hardcoding, it would allow adding any future column without altering the table structure.

Architecture: Keep the logic decoupled, ensuring that the frontend only consumes data from the backend without depending on a fixed column structure.

### 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

If we received only a list of legislators or bills:

I would create a backend function to dynamically generate a CSV from JSON data, using libraries like pandas or csv.

The endpoint would accept the provided list, fetch the corresponding details (such as votes or co-sponsors), and return a ready-to-download CSV.

The frontend would make a request to this endpoint and allow the user to download the CSV without manually handling files.

This approach keeps the application scalable and flexible.

### 4. How long did you spend working on the assignment?

I spent approximately 8 to 12 hours on the complete development, including:

Backend configuration and endpoints: 5–6 hours

Frontend development and API integration: 1–2 hours

Testing, CORS adjustments, Docker, and deployment scripts: 1–2 hours