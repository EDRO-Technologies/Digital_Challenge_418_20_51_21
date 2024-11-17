import {
	CartesianGrid,
	Line,
	LineChart,
	Tooltip,
	XAxis,
	YAxis,
} from "recharts";

const Response = ({ data, title }) => {
	return (
		<div className="flex flex-col justify-center mt-16">
			<h3 className="text-sm text-gray-500 mb-5 text-center">{title}</h3>
			<LineChart width={800} height={400} data={data}>
				<CartesianGrid strokeDasharray="3 3" />
				<XAxis dataKey="name" />
				<YAxis />
				<Tooltip />
				<Line type="monotone" dataKey="value" stroke="#0026ff" />
			</LineChart>
		</div>
	);
};

export default Response;
