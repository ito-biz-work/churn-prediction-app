import { useState } from 'react';
import CustomerList,{ type Customer } from './components/CustomerList';
import PredictionPanel from './components/PredictionPanel';

function App() {
  const [selectedCustomer, setSelectedCustomer] = useState<Customer| null>(null);

  return (
    <div className="flex h-screen">
      <div className="w-1/2 border-r">
        {/* CustomerListに「クリックされたらここを更新する」という指示を渡します */}
        <CustomerList onSelect={setSelectedCustomer} />
      </div>
      <div className="w-1/2 bg-gray-50">
        <PredictionPanel customer={selectedCustomer} />
      </div>
    </div>
  );
}
export default App;