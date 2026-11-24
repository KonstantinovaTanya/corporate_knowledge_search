
from app.core.database import get_connection


def init_database():
    """Создаёт таблицы базы данных."""

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
        INSERT INTO Roles (name)
        VALUES
            ('employee'),
            ('department_head'),
            ('admin')
    """)

    # Заполнение уровней доступа
    cursor.execute("""
        INSERT INTO AccessLevels (name)
        VALUES
            ('all'),
            ('department'),
            ('admin')
    """)

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    init_database()
    print("Таблицы базы данных успешно созданы.")
