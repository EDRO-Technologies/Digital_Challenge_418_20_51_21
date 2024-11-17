import { useQuery, useQueryClient } from "react-query";
import { refreshUser } from "../../api/auth";
import { getEnergyConsumption } from "../../api/charts";

export const useEnergyConsumption = () => {
	const queryClient = useQueryClient();

	const { data, isLoading, isSuccess, isError, error, refetch } = useQuery({
		queryKey: ["energy_consumption"],
		queryFn: () => getEnergyConsumption(),
		select: data => data.data,
		retry: false,
		onError: async error => {
			if (error.status === 401) {
				try {
					await refreshUser();
					queryClient.invalidateQueries(["energy_consumption"]);
				} catch {
					window.location.href = "/auth";
				}
			}
		},
	});

	return {
		energyData: data,
		energyIsLoading: isLoading,
		energyIsSuccess: isSuccess,
		energyIsError: isError,
		energyError: error,
		energyRefetch: refetch,
	};
};
