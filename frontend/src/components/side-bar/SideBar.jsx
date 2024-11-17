import { Listbox, ListboxItem } from "@nextui-org/react";
import { useNavigate } from "react-router-dom";
import sngLogoSrc from "../../assets/sng-logo.png";
import { useLogout } from "../../hooks/auth/useLogout.js";
import ListboxWrapper from "./ListboxWrapper.jsx";

const SideBar = () => {
	const navigate = useNavigate();

	const { logoutRefetch } = useLogout();

	return (
		<ListboxWrapper>
			<div className="w-full flex justify-center my-7">
				<img className="w-36" src={sngLogoSrc} alt="sng-logo" />
			</div>
			<Listbox variant="flat" className="h-full" color="primary">
				<ListboxItem
					key="main"
					onClick={() => navigate("main", { replace: false })}
				>
					Главная
				</ListboxItem>
				<ListboxItem
					key="analytics"
					onClick={() => navigate("analytics", { replace: false })}
				>
					Аналитика
				</ListboxItem>
				<ListboxItem
					key="map"
					onClick={() => navigate("map", { replace: false })}
				>
					Карта
				</ListboxItem>
				<ListboxItem
					key="imports-exports"
					onClick={() => navigate("imports-exports", { replace: false })}
					showDivider
				>
					Импорт и экспорт
				</ListboxItem>
				<ListboxItem
					key="logout"
					className="text-danger mt-auto"
					color="danger"
					onClick={() => logoutRefetch()}
				>
					Выйти
				</ListboxItem>
			</Listbox>
		</ListboxWrapper>
	);
};

export default SideBar;
