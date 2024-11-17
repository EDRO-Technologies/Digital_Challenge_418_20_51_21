import { Map, Placemark, YMaps } from "@pbe/react-yandex-maps";

const MapComponent = ({ objects, mapRef }) => {
	return (
		<YMaps>
			<Map
				width={700}
				height={450}
				instanceRef={ref => (mapRef.current = ref)}
				defaultState={{
					center: [61.24178, 73.393029],
					zoom: 9,
				}}
			>
				{objects.map((obj, i) => (
					<Placemark key={i} geometry={obj.coord} />
				))}
			</Map>
		</YMaps>
	);
};

export default MapComponent;
