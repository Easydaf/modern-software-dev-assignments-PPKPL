# Week 3 - DummyData MCP Server

Server MCP lokal ini membungkus JSONPlaceholder API secara gratis untuk mengambil data profil pengguna dan postingan secara dinamis. Server ini menggunakan transport STDIO dan dibangun menggunakan framework FastMCP.

## Cara Mengatur dan Menjalankan (Menggunakan Conda)
1. Buat conda environment baru: `conda create --name mcp-week3 python=3.10 -y`
2. Aktifkan environment: `conda activate mcp-week3`
3. Instal dependencies menggunakan pip: `pip install mcp httpx`
4. Jalankan inspector untuk menguji server secara lokal: `npx @modelcontextprotocol/inspector python server/main.py`

## Referensi Tools

Server ini mengekspos dua tools utama:

1. **`get_user_info`**
   - **Parameter**: `user_id` (integer, masukkan angka 1 sampai 10)
   - **Perilaku**: Menerima ID pengguna dan mengembalikan detail informasi pengguna (nama, email, dan nama perusahaan tempat bekerja).
   - **Contoh input**: `{"user_id": 1}`

2. **`get_user_posts`**
   - **Parameter**: `user_id` (integer, masukkan angka 1 sampai 10)
   - **Perilaku**: Menerima ID pengguna dan mengekstrak 3 judul postingan teratas yang dibuat oleh pengguna tersebut.
   - **Contoh input**: `{"user_id": 1}`