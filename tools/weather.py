import os
import httpx

def search_weather_tools(mcp):
    DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "employees")
    os.makedirs(DATA_DIR, exist_ok=True)

    @mcp.tool()
    async def get_weather(location: str) -> str:
        """특정 도시나 지역의 현재 날씨 정보를 조회합니다.

        Args:
            location: 날씨를 조회할 도시 이름 (예: 'Seoul', 'Tokyo', 'London')
        """
        try:
            # wttr.in 무료 날씨 API 활용 (JSON 포맷)
            async with httpx.AsyncClient() as client:
                url = f"https://wttr.in/{location}?format=j1"
                response = await client.get(url, timeout=5.0)

                if response.status_code != 200:
                    return f"'{location}' 지역의 날씨 정보를 찾을 수 없습니다."

                data = response.json()
                current = data["current_condition"][0]

                temp_c = current["temp_C"]
                weather_desc = current["weatherDesc"][0]["value"]
                humidity = current["humidity"]

                return (
                    f"[{location} 현재 날씨]\n"
                    f"- 기온: {temp_c}°C\n"
                    f"- 상태: {weather_desc}\n"
                    f"- 습도: {humidity}%"
                )

        except Exception as e:
            return f"날씨 정보 조회 중 오류가 발생했습니다: {str(e)}"