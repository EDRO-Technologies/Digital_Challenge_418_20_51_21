import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Analytics from "../../views/analytics/Analytics";
import AuthView from "../../views/auth/auth";
import Home from "../../views/home/home";
import MapView from "../../views/map/Map";
import Foundation from "../foundation/Foundation";

const MainContent = () => {
	return (
		<BrowserRouter>
			<Routes>
				<Route path="/auth" element={<AuthView />}></Route>
				<Route path="/" element={<Foundation />}>
					<Route path="main" element={<Home />}></Route>
					<Route path="analytics" element={<Analytics />} />
					<Route path="map" element={<MapView />} />
					<Route path="imports-exports" element={<div>imports-exports</div>} />
					<Route path="*" element={<Navigate replace to="/main" />} />
				</Route>
			</Routes>
		</BrowserRouter>
	);
};

export default MainContent;
