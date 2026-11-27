
from app.core.database import get_connection
from app.core.config import SQL_DATABASE


def create_database():
    """Создаёт базу данных, если она ещё не существует."""

    connection = get_connection("master")
    cursor = connection.cursor()

    database_name = SQL_DATABASE.replace("]", "]]")
    database_literal = SQL_DATABASE.replace("'", "''")

    cursor.execute(f"""
        IF DB_ID(N'{database_literal}') IS NULL
        BEGIN
            CREATE DATABASE [{database_name}]
        END
    """)

    connection.commit()
    cursor.close()
    connection.close()


def init_database():
    """Создаёт таблицы и заполняет справочники."""

    # Создание базы данных при необходимости
    create_database()

    connection = get_connection()
    cursor = connection.cursor()

    # 1. Роли пользователей
    cursor.execute("""
        IF OBJECT_ID('Roles', 'U') IS NULL
        BEGIN
            CREATE TABLE Roles (
                id INT IDENTITY(1,1) PRIMARY KEY,
                name NVARCHAR(50) NOT NULL UNIQUE
            );
        END
    """)

    # 2. Подразделения
    cursor.execute("""
        IF OBJECT_ID('Departments', 'U') IS NULL
        BEGIN
            CREATE TABLE Departments (
                id INT IDENTITY(1,1) PRIMARY KEY,
                name NVARCHAR(300) NOT NULL UNIQUE
            );
        END
    """)

    # 3. Уровни доступа
    cursor.execute("""
        IF OBJECT_ID('AccessLevels', 'U') IS NULL
        BEGIN
            CREATE TABLE AccessLevels (
                id INT IDENTITY(1,1) PRIMARY KEY,
                name NVARCHAR(50) NOT NULL UNIQUE
            );
        END
    """)

    # 4. Пользователи
    cursor.execute("""
        IF OBJECT_ID('Users', 'U') IS NULL
        BEGIN
            CREATE TABLE Users (
                id NVARCHAR(100) PRIMARY KEY,
                role_id INT NOT NULL,
                department_id INT NOT NULL,

                FOREIGN KEY (role_id) REFERENCES Roles(id),
                FOREIGN KEY (department_id) REFERENCES Departments(id)
            );
        END
    """)

    # 5. Документы
    cursor.execute("""
        IF OBJECT_ID('Documents', 'U') IS NULL
        BEGIN
            CREATE TABLE Documents (
                id NVARCHAR(20) PRIMARY KEY,
                title NVARCHAR(500) NOT NULL,
                filename NVARCHAR(500) NOT NULL,
                department_id INT NOT NULL,
                access_level_id INT NOT NULL,
                author_id NVARCHAR(100) NULL,
                content NVARCHAR(MAX) NOT NULL,

                FOREIGN KEY (department_id) REFERENCES Departments(id),
                FOREIGN KEY (access_level_id) REFERENCES AccessLevels(id),
                FOREIGN KEY (author_id) REFERENCES Users(id)
            );
        END
    """)

    # 6. История запросов
    cursor.execute("""
        IF OBJECT_ID('QueryHistory', 'U') IS NULL
        BEGIN
            CREATE TABLE QueryHistory (
                id INT IDENTITY(1,1) PRIMARY KEY,
                user_id NVARCHAR(100) NOT NULL,
                query_text NVARCHAR(MAX) NOT NULL,
                created_at DATETIME2 NOT NULL DEFAULT SYSDATETIME(),

                FOREIGN KEY (user_id) REFERENCES Users(id)
            );
        END
    """)

    # Заполнение справочника ролей
    cursor.execute("""
        IF NOT EXISTS (SELECT 1 FROM Roles)
        BEGIN
            INSERT INTO Roles (name)
            VALUES
                ('employee'),
                ('department_head'),
                ('admin')
        END
    """)

    # Заполнение уровней доступа
    cursor.execute("""
        IF NOT EXISTS (SELECT 1 FROM AccessLevels)
        BEGIN
            INSERT INTO AccessLevels (name)
            VALUES
                ('all'),
                ('department'),
                ('admin')
        END
    """)

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    init_database()
    print("База данных и таблицы успешно созданы.")
