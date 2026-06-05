import { useState } from 'react';

function App() {
  const [result, setResult] = useState<string>("");

  const handleClick = async () => {
    try {
      // API
      const response = await fetch("http://127.0.0.1:8000/api/v1/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        // ダミーデータ
        body: JSON.stringify({
            "state": "NJ",
            "area_code": "area_code_415",
            "account_length": 128,
            "international_plan": "no",
            "voice_mail_plan": "yes",
            "number_vmail_messages": 25,
            "total_day_minutes": 265.1,
            "total_day_calls": 110,
            "total_day_charge": 45.07,
            "total_eve_minutes": 197.4,
            "total_eve_calls": 99,
            "total_eve_charge": 16.78,
            "total_night_minutes": 244.7,
            "total_night_calls": 91,
            "total_night_charge": 11.01,
            "total_intl_minutes": 10.0,
            "total_intl_calls": 3,
            "total_intl_charge": 2.7,
            "number_customer_service_calls": 1
        }),
      });

      const data = await response.json();
      console.log("APIからの返事:", data);
      setResult(JSON.stringify(data));
    } catch (error) {
      console.error("通信エラー:", error);
    }
  };

  return (
    <div>
      <h1>API連携テスト</h1>
      <button onClick={handleClick}>予測を実行</button>
      <p>結果: {result}</p>
    </div>
  );
}

export default App;