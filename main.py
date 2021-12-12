import qrcode
import psycopg2
input_data = ""


def qr_gen():
    qr = qrcode.QRCode(
        version=1,
        box_size=100,
        border=5)
    qr.add_data(input_data)
    qr.make(fit=True)

    img = qr.make(fill='black', back_color='white')
    img.save('qrcode001.png')


def register():
    serial_number = input('Please enter the serial number: ')
    manufacturer = input('Please enter the manufacturer: ')
    model = input('Please enter the model: ')
    color = input('Please enter the color: ')


def human_register():
    email = input('Please enter your email: ')
    psswd = input('Please enter a password: ')
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="admin",
                                      port="5432",
                                      database="postgres")
        cursor = connection.cursor()
        postgres_insert_query = "INSERT INTO users (email, password) VALUES (%s, %s)"
        record_to_insert = (email, psswd)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count)
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection is closed")


if __name__ == "__main__":
    human_register()