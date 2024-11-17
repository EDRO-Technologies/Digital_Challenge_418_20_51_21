import {
	CartesianGrid,
	Line,
	LineChart,
	Tooltip,
	XAxis,
	YAxis,
} from "recharts";

const Indicator = ({ data, color }) => {
	return (
		<LineChart width={300} height={150} data={data}>
			<CartesianGrid strokeDasharray="3 3" />
			<XAxis dataKey="name" />
			<YAxis />
			<Tooltip />
			<Line type="monotone" dataKey="value" stroke={color} />
		</LineChart>
	);
};

export default Indicator;
