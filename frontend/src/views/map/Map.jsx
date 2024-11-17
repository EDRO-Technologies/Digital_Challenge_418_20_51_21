import { useRef } from "react";
import Objects from "../../components/lists/objects/Objects";
import MapComponent from "../../components/map/MapComponent";

const MapView = () => {
	const mapRef = useRef(null);

	const handleButtonClick = newCoord => {
		mapRef.current.setCenter(newCoord);
	};

	const objs = [
		{ name: "Куст № 711", coord: [61.135191, 72.705314] },
		{ name: "Куст № 691", coord: [61.135191, 75.547135] },
		{ name: "Куст № 5", coord: [61.135191, 75.547135] },
		{ name: "Куст № 619", coord: [61.135191, 75.547135] },
		{ name: "Куст № 160", coord: [61.135191, 75.547135] },
		{ name: "Куст № 617", coord: [61.135191, 75.547135] },
		{ name: "Куст № 206", coord: [61.135191, 75.547135] },
		{ name: "Куст № 337", coord: [61.135191, 75.547135] },
	];

	return (
		<div className="flex flex-col w-full h-full items-center overflow-y-auto max-h-screen">
			<h1 className="my-10">Карта</h1>
			<div className="flex justify-center gap-10">
				<div>
					<MapComponent objects={objs} mapRef={mapRef} />
				</div>
				<div className="flex flex-col items-center">
					<h3 className="text-sm text-gray-500 mb-3">Список объектов</h3>
					<Objects objects={objs} handleButtonClick={handleButtonClick} />
				</div>
			</div>
		</div>
	);
};

export default MapView;
