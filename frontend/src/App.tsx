import { useState } from 'react';
import CustomerList, { type Customer } from './components/CustomerList';
import PredictionPanel from './components/PredictionPanel';

function App() {
  const [selectedCustomer, setSelectedCustomer] = useState<Customer | null>(null);

  return (
    <div className="flex flex-col min-h-screen bg-slate-50">
      {/* ヘッダー */}
      <header className="bg-slate-800 p-4 shadow-md">
        <h1 className="text-xl font-bold text-white tracking-wide">
          顧客分析ダッシュボード
        </h1>
      </header>

      {/* メインコンテンツ */}
      <main className="grow p-6 flex gap-6">
        <div className="w-1/2">
          <CustomerList onSelect={setSelectedCustomer} />
        </div>
        <div className="w-1/2">
          <PredictionPanel customer={selectedCustomer} />
        </div>
      </main>

      {/* フッター */}
      <footer className="bg-slate-200 border-t border-slate-300 p-4 text-center text-sm text-slate-600">
        © 2026 Customer Insights System
      </footer>
    </div>
  );
}

export default App;