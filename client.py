# client.py
import asyncio
import os
import shutil
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# 데이터 초기화 함수
def clear_data():
    folders = ["data/employees", "data/todos"]
    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            os.makedirs(folder)
    # todo_list.json도 초기화
    if os.path.exists("data/todo_list.json"):
        os.remove("data/todo_list.json")
    print("--- 모든 데이터 초기화 완료 ---")

async def run_client():
    clear_data() # 테스트 시작 전 클리어
    
    server_params = StdioServerParameters(command="python", args=["server.py"])

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1. 직원 정보 저장 테스트
            print("\n[테스트] 직원 정보 저장")
            res1 = await session.call_tool("save_employee_info", arguments={
                "name": "김민수", 
                "content": "ID: 1001\n부서: 개발\n직책: 백엔드 엔지니어"
            })
            print(res1)

            # 2. 직원 정보 조회 테스트
            print("\n[테스트] 직원 정보 검색")
            res2 = await session.call_tool("search_employee_info", arguments={"name": "김민수"})
            print(f"검색 결과: {res2}")

            # 3. 할 일 추가 테스트
            print("\n[테스트] 할 일 추가")
            res3 = await session.call_tool("add_todo", arguments={"task": "MCP 서버 배포", "assignee": "김민수"})
            print(res3)

            # 4. 할 일 조회 테스트
            print("\n[테스트] 할 일 목록 조회")
            res4 = await session.call_tool("list_todos", arguments={"assignee": "김민수"})
            print(f"조회 결과: {res4}")

            print("\n--- 모든 테스트 성공적으로 완료 ---")

if __name__ == "__main__":
    asyncio.run(run_client())