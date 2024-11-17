import { useQuery, useQueryClient } from "react-query";
import { refreshUser } from "../../api/auth";
import { getEnergyIntensiveTop } from "../../api/top";

export const useEnergyIntensiveTop = () => {
	const queryClient = useQueryClient();

	const { data, isLoading, isSuccess, isError, error, refetch } = useQuery({
		queryKey: ["most_energy_intensive"],
		queryFn: () => getEnergyIntensiveTop(),
		select: data => data.data,
		retry: false,
		onError: async error => {
			if (error.status === 401) {
				try {
					await refreshUser();
					queryClient.invalidateQueries(["most_energy_intensive"]);
				} catch {
					window.location.href = "/auth";
				}
			}
		},
	});

	return {
		energyTopData: data,
		energyTopIsLoading: isLoading,
		energyTopIsSuccess: isSuccess,
		energyTopIsError: isError,
		energyTopError: error,
		energyTopRefetch: refetch,
	};
};
