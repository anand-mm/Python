import psycopg2
import subprocess

def prevent_folder_actions(folder_path):
    try:
        # Prevent copying, moving, deleting
        subprocess.run(["setfacl", "-d", "-m", "u::rwx,u::-w-", folder_path], check=True)

        # Prevent changing ownership, changing group ownership, changing permissions
        subprocess.run(["setfacl", "-m", "u::rwx,u::-w-", folder_path], check=True)

        print(f"Permissions updated for folder: {folder_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def get_folder_paths_from_database():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute("SELECT folder_path FROM folder_path")
    folder_paths = [row[0] for row in cur.fetchall()]
    conn.close()

    return folder_paths

if __name__ == "__main__":
    folder_paths = get_folder_paths_from_database()
    for folder_path in folder_paths:
        prevent_folder_actions(folder_path)

