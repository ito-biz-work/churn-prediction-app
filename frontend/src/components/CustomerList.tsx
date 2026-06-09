export type Customer = {
  id: number;
  name: string;
  code: string;
};

// 仮データ
const customers: Customer[] = [
  { id: 1, name: "田中 太郎", code: "CUST001" },
  { id: 2, name: "佐藤 花子", code: "CUST002" },
  { id: 3, name: "鈴木 一郎", code: "CUST003" },
];


// 型を定義
interface CustomerListProps {
  onSelect: (customer: Customer) => void;
}

export default function CustomerList({ onSelect }: CustomerListProps) {
  return (
    <div className="bg-white p-6 shadow-md border border-gray-200 rounded-lg">
      <h2 className="text-2xl font-bold mb-4">顧客一覧</h2>
      
      {/* 枠線と角丸を維持しつつ、内側のフォントサイズを統一 */}
      <div className="border border-gray-200 rounded-md overflow-hidden">
        
        {/* ヘッダー部分：text-sm にして落ち着いた印象に */}
        <div className="grid grid-cols-4 gap-2 p-3 bg-gray-50 border-b border-gray-200 font-semibold text-sm text-gray-600 uppercase tracking-wider">
          <div>ID</div>
          <div>氏名</div>
          <div>顧客コード</div>
          <div></div>
        </div>

        {/* 顧客リスト：text-base で読みやすく */}
        {customers.map((customer) => (
          <div key={customer.id} className="grid grid-cols-4 gap-2 p-3 border-b border-gray-100 items-center last:border-b-0 text-base text-gray-900">
            <div>{customer.id}</div>
            <div>{customer.name}</div>
            <div>{customer.code}</div>
            <button 
              className="bg-blue-600 text-white px-3 py-1 rounded hover:bg-blue-700 transition text-sm shadow-sm"
              onClick={() => onSelect(customer)}
            >
              実行
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}