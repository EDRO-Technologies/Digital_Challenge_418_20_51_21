import { useEffect } from "react";
import { Outlet, useNavigate } from "react-router-dom";
import SideBar from "../../components/side-bar/SideBar";

export function Foundation() {
	const navigate = useNavigate();
	useEffect(() => {
		navigate("/main");
	}, []);

	return (
		<div className="flex w-full h-full">
			<SideBar />
			<Outlet />
		</div>
	);
}

export default Foundation;
