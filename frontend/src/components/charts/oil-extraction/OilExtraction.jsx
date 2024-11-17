import {
	Area,
	AreaChart,
	CartesianGrid,
	Tooltip,
	XAxis,
	YAxis,
} from "recharts";

const OilExtraction = ({ data }) => {
	return (
		<AreaChart width={800} height={400} data={data}>
			<defs>
				<linearGradient id="colorPresence" x1="0" y1="0" x2="0" y2="1">
					<stop offset="5%" stopColor="#8884d8" stopOpacity={0.8} />
					<stop offset="95%" stopColor="#8884d8" stopOpacity={0} />
				</linearGradient>
				<linearGradient id="colorPlan" x1="0" y1="0" x2="0" y2="1">
					<stop offset="5%" stopColor="#82ca9d" stopOpacity={0.8} />
					<stop offset="95%" stopColor="#82ca9d" stopOpacity={0} />
				</linearGradient>
			</defs>
			<XAxis dataKey="name" />
			<YAxis />
			<CartesianGrid strokeDasharray="3 3" />
			<Tooltip />
			<Area
				type="monotone"
				dataKey="presence"
				stroke="#8884d8"
				fillOpacity={1}
				fill="url(#colorPresence)"
			/>
			<Area
				type="monotone"
				dataKey="plan"
				stroke="#82ca9d"
				fillOpacity={1}
				fill="url(#colorPlan)"
			/>
		</AreaChart>
	);
};

export default OilExtraction;
