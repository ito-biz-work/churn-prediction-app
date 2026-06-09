// 顧客データの型を定義
interface Customer {
  id: number;
  name: string;
  code: string;
}

interface PredictionPanelProps {
  customer: Customer | null;
}

export default function PredictionPanel({ customer }: PredictionPanelProps) {
  // customer が選択されていない場合の表示
  if (!customer) {
    return (
      <div className="bg-white p-8 shadow-md border border-gray-200 rounded-lg text-gray-500 text-center">
        顧客を選択すると、ここに予測結果が表示されます。
      </div>
    );
  }

  return (
    <div className="bg-white p-6 shadow-md border border-gray-200 rounded-lg">
      <h2 className="text-2xl font-bold mb-6">予測結果詳細</h2>
      
      {/* 退会確率の目立つ表示 */}
      <div className="bg-gray-50 p-6 rounded-md border border-gray-200 mb-6">
        <div className="text-sm font-semibold text-gray-600 uppercase tracking-wide mb-1">退会確率</div>
        <div className="text-4xl font-extrabold text-red-600">85%</div>
      </div>

      {/* 顧客属性情報 */}
      <div className="border border-gray-200 rounded-md overflow-hidden">
        <h3 className="bg-gray-50 p-3 font-semibold text-sm text-gray-600 border-b border-gray-200 uppercase tracking-wide">
          顧客属性情報
        </h3>
        <div className="p-4 space-y-3 text-base text-gray-900">
          <div className="flex">
            <span className="w-24 font-medium text-gray-500">氏名:</span>
            <span>{customer.name}</span>
          </div>
          <div className="flex">
            <span className="w-24 font-medium text-gray-500">居住州:</span>
            <span>NJ</span>
          </div>
          <div className="flex">
            <span className="w-24 font-medium text-gray-500">エリアコード:</span>
            <span>area_code_415</span>
          </div>
          <div className="flex">
            <span className="w-24 font-medium text-gray-500">契約期間:</span>
            <span>55ヶ月</span>
          </div>
        </div>
      </div>
    </div>
  );
}