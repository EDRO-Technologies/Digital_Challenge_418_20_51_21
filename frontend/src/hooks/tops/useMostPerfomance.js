import { useQuery, useQueryClient } from "react-query";
import { refreshUser } from "../../api/auth";
import { getMostPerfomance } from "../../api/top";

export const useMostPerfomance = () => {
	const queryClient = useQueryClient();

	const { data, isLoading, isSuccess, isError, error, refetch } = useQuery({
		queryKey: ["most_perfomance"],
		queryFn: () => getMostPerfomance(),
		select: data => data.data,
		retry: false,
		onError: async error => {
			if (error.status === 401) {
				try {
					await refreshUser();
					queryClient.invalidateQueries(["most_perfomance"]);
				} catch {
					window.location.href = "/auth";
				}
			}
		},
	});

	return {
		performanceData: data,
		performanceIsLoading: isLoading,
		performanceIsSuccess: isSuccess,
		performanceIsError: isError,
		performanceError: error,
		performanceRefetch: refetch,
	};
};
