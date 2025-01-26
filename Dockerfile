# Step 1: Use an official Python runtime as a parent image
FROM python:3.11-slim

# Step 2: Set the working directory in the container
WORKDIR /usr/src/app

# Step 3: Copy only the requirements file first (this minimizes rebuilds)
COPY requirements.txt ./

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application files
COPY . .

# Step 6: Copy the local SQLite database into the container
COPY db.sqlite3 /usr/src/app/db.sqlite3

# Step 7: Run migrations (to ensure consistency)
#RUN python manage.py makemigrations
RUN python manage.py migrate

# Step 8: Expose port 8000 to access the app outside the container
EXPOSE 8000

# Step 9: Set the default command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
