import { Button, Input } from "@nextui-org/react";
import Response from "../../components/charts/response/Response";

const Analytics = () => {
	const data = [
		{
			name: "01.11",
			value: 10000,
		},
		{
			name: "02.11",
			value: 8000,
		},
		{
			name: "03.11",
			value: 6000,
		},
		{
			name: "04.11",
			value: 7500,
		},
		{
			name: "05.11",
			value: 7000,
		},
		{
			name: "06.11",
			value: 8500,
		},
		{
			name: "07.11",
			value: 9000,
		},
	];

	return (
		<div className="flex flex-col w-full h-full items-center overflow-y-auto max-h-screen">
			<h1 className="my-10">Аналитика</h1>
			<div className="flex w-full px-28">
				<Input
					color="default"
					size="md"
					type="text"
					placeholder="Какая информация Вас интересует?"
					className="mr-5"
				/>
				<Button size="md" color="primary" variant="solid">
					Запросить
				</Button>
			</div>
			<Response
				data={data}
				title={"Возможная добыча нефти во 2 половине 2024 года (в куб. м)"}
			/>
		</div>
	);
};

export default Analytics;
