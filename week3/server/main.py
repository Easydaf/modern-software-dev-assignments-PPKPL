from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("DummyData")

@mcp.tool()
def get_user_info(user_id: int) -> str:
    """Dapatkan informasi detail pengguna berdasarkan ID (masukkan angka 1 sampai 10)."""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = httpx.get(url, timeout=10.0)
        response.raise_for_status()
        data = response.json()
        return f"Nama: {data['name']}\nEmail: {data['email']}\nPerusahaan: {data['company']['name']}"
    except httpx.HTTPStatusError:
        return "Pengguna tidak ditemukan."
    except httpx.RequestError as exc:
        return f"Gagal menghubungi API: {exc}"

@mcp.tool()
def get_user_posts(user_id: int) -> str:
    """Dapatkan daftar postingan dari seorang pengguna berdasarkan ID (masukkan angka 1 sampai 10)."""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}/posts"
    try:
        response = httpx.get(url, timeout=10.0)
        response.raise_for_status()
        data = response.json()
        if not data:
            return "Tidak ada postingan."
            
        # Mengambil 3 judul postingan teratas
        titles = [f"- {post['title']}" for post in data[:3]] 
        return f"3 Postingan Teratas:\n" + "\n".join(titles)
    except httpx.HTTPStatusError:
        return "Data postingan tidak ditemukan."
    except httpx.RequestError as exc:
        return f"Gagal menghubungi API: {exc}"

if __name__ == "__main__":
    mcp.run()