import { NextUIProvider } from "@nextui-org/react";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { QueryClientProvider } from "react-query";
import { queryClient } from "./api/query-client";
import Root from "./components/Root";
import "./styles/index.css";

createRoot(document.getElementById("root")).render(
	<StrictMode>
		<QueryClientProvider client={queryClient}>
			<NextUIProvider>
				<Root />
			</NextUIProvider>
		</QueryClientProvider>
	</StrictMode>
);
