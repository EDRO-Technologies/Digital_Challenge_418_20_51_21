import { CircularProgress } from "@nextui-org/react";
import Indicator from "../../components/charts/indicator/Indicator";
import OilExtraction from "../../components/charts/oil-extraction/OilExtraction";
import Top from "../../components/lists/top/Top";
import { useDebit } from "../../hooks/charts/useDebit";
import { useEnergyConsumption } from "../../hooks/charts/useEnergyConsumption";
import { useEnergyIntensiveTop } from "../../hooks/tops/useEnergyIntensiveTop";
import { useMostPerfomance } from "../../hooks/tops/useMostPerfomance";

const Home = () => {
	const { debitData, debitIsSuccess, debitIsLoading } = useDebit();
	const { energyData, energyIsSuccess, energyIsLoading } =
		useEnergyConsumption();
	const { energyTopData, energyTopIsSuccess, energyTopIsLoading } =
		useEnergyIntensiveTop();
	const { performanceData, performanceIsSuccess, performanceIsLoading } =
		useMostPerfomance();

	return (
		<div className="flex flex-col w-full h-full items-center overflow-y-auto max-h-screen">
			<h1 className="my-10">Главная</h1>
			<div className="flex w-full justify-center gap-10">
				<div className="flex flex-col items-center">
					<h3 className="text-sm text-gray-500 mb-2">
						Кол-во добытой нефти (в м<sup>3</sup>)
					</h3>
					{debitIsLoading && (
						<CircularProgress size="lg" aria-label="Loading..." />
					)}
					{debitIsSuccess && <OilExtraction data={debitData.days} />}
				</div>
				<div className="flex flex-col items-center">
					<h3 className="text-sm text-gray-500 mb-2">Топ 10</h3>
					{(energyTopIsLoading || performanceIsLoading) && (
						<CircularProgress size="lg" aria-label="Loading..." />
					)}
					{energyTopIsSuccess && performanceIsSuccess && (
						<Top
							productive={performanceData.well_names}
							energyIntensive={energyTopData.well_names}
						/>
					)}
				</div>
			</div>
			<div className="flex w-full justify-center mt-10 gap-24">
				<div className="flex flex-col items-center">
					<h3 className="text-xs text-gray-500 mb-2">
						Энергопотребление (в Квт/ч)
					</h3>
					{energyIsLoading && (
						<CircularProgress size="lg" aria-label="Loading..." />
					)}
					{energyIsSuccess && (
						<Indicator data={energyData.days} color={"#ffa600"} />
					)}
				</div>
				<div className="flex flex-col items-center">
					<h3 className="text-xs text-gray-500 mb-2">
						Затраты на содрежание (в млн. руб.)
					</h3>
					{energyIsLoading && (
						<CircularProgress size="lg" aria-label="Loading..." />
					)}
					{energyIsSuccess && (
						<Indicator data={energyData.days} color={"#c81a1a"} />
					)}
				</div>
				<div className="flex flex-col items-center">
					<h3 className="text-xs text-gray-500 mb-2">
						Суточная наработка насоса (в у.е.)
					</h3>
					{energyIsLoading && (
						<CircularProgress size="lg" aria-label="Loading..." />
					)}
					{energyIsSuccess && (
						<Indicator data={energyData.days} color={"#00fde8"} />
					)}
				</div>
			</div>
		</div>
	);
};

export default Home;
