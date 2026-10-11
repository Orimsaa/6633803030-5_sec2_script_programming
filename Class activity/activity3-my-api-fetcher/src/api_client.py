# my-api-fetcher/src/api_client.py
"""
APIClient: ส่ง HTTP GET ไปยัง JSONPlaceholder (REST API สาธารณะสำหรับฝึก)
แล้วแปลง JSON เป็น dict/list ของ Python พร้อมจัดการข้อผิดพลาดของเครือข่ายและ HTTP status
"""
import json
import os
from typing import Any, Dict, List, Optional

import requests


class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self, base_url: Optional[str] = None, timeout: int = 10):
        self.base_url = (base_url or self.BASE_URL).rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()  # ใช้ connection ซ้ำ ทำให้เรียกหลายครั้งได้เร็วขึ้น

    def _make_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Any]:
        """ส่ง GET request และคืนค่า JSON ที่แปลงแล้ว หรือ None ถ้าเกิดข้อผิดพลาด"""
        url = f"{self.base_url}{endpoint}"
        print(f"[INFO] GET {url}" + (f" params={params}" if params else ""))
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()  # 4xx / 5xx -> HTTPError
            return response.json()
        except requests.exceptions.HTTPError as e:
            code = e.response.status_code if e.response is not None else "?"
            print(f"[ERROR] HTTP Error {code}: {'resource not found' if code == 404 else e}")
        except requests.exceptions.ConnectionError:
            print("[ERROR] Connection Error: cannot reach the server. Check your internet connection.")
        except requests.exceptions.Timeout:
            print(f"[ERROR] Timeout: the server did not respond within {self.timeout} seconds.")
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Request failed: {e}")
        except json.JSONDecodeError:
            print("[ERROR] The response is not valid JSON.")
        return None

    # --- Endpoints จาก Lab -------------------------------------------------
    def fetch_single_todo(self, todo_id: int) -> Optional[Dict[str, Any]]:
        """GET /todos/{id}"""
        return self._make_request(f"/todos/{todo_id}")

    def fetch_all_posts(self) -> Optional[List[Dict[str, Any]]]:
        """GET /posts"""
        return self._make_request("/posts")

    def fetch_user_todos(self, user_id: int) -> Optional[List[Dict[str, Any]]]:
        """GET /todos?userId={id} (query parameter)"""
        return self._make_request("/todos", params={"userId": user_id})

    # --- Endpoints เพิ่มเติม (Assignment Task 1-2) -----------------------
    def fetch_user_profile(self, user_id: int) -> Optional[Dict[str, Any]]:
        """GET /users/{id} — คืนค่า None เมื่อไม่พบผู้ใช้ (API ตอบ 404)"""
        return self._make_request(f"/users/{user_id}")

    def fetch_post_comments(self, post_id: int) -> Optional[List[Dict[str, Any]]]:
        """GET /posts/{id}/comments"""
        return self._make_request(f"/posts/{post_id}/comments")


def export_to_json_file(filename: str, data: Any) -> bool:
    """(Assignment Task 3) บันทึกข้อมูลเป็นไฟล์ JSON แบบ UTF-8 อ่านง่าย รองรับภาษาไทย"""
    try:
        folder = os.path.dirname(filename)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        shown = os.path.relpath(filename) if os.path.isabs(filename) else filename
        print(f"[OK] Saved {len(data) if isinstance(data, list) else 1} record(s) to {shown}")
        return True
    except (IOError, PermissionError) as e:
        print(f"[ERROR] Could not write file '{filename}': {e}")
    except TypeError as e:
        print(f"[ERROR] Data is not JSON serializable: {e}")
    return False
