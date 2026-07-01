import { StrictMode, type ErrorInfo  } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { ErrorBoundary} from "react-error-boundary";
import "./index.css";
import { Provider } from "@/components/ui/provider";
import { ErrorFallback } from "@/components/ui/ErrorFallback";
import App from "./App.tsx";

// エラー発生時の関数
const logError = (error: unknown, info: ErrorInfo) => {
  console.error(error, info.componentStack);
};

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Provider>
      <BrowserRouter>
        <ErrorBoundary FallbackComponent={ErrorFallback} onError={logError}>
          <App />
        </ErrorBoundary>
      </BrowserRouter>
    </Provider>
  </StrictMode>,
);
