export interface Customer {
  id: number;

  // --- システム項目 ---
  createdAt: string;
  updatedAt: string;

  // --- 退会確率 ---
  churnProbability: number;

  // --- 顧客属性 ---
  customerName: string;
  customerCode: string;
  state: string;
  areaCode: string;
  accountLength: number;

  // --- プラン情報 ---
  internationalPlan: string;
  voiceMailPlan: string;
  numberVmailMessages: number;

  // --- 通話利用状況 ---
  totalDayMinutes: number;
  totalDayCalls: number;
  totalDayCharge: number;

  totalEveMinutes: number;
  totalEveCalls: number;
  totalEveCharge: number;

  totalNightMinutes: number;
  totalNightCalls: number;
  totalNightCharge: number;

  totalIntlMinutes: number;
  totalIntlCalls: number;
  totalIntlCharge: number;

  // --- サポート状況 ---
  numberCustomerServiceCalls: number;
}