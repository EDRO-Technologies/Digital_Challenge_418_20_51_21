import { useQuery, useQueryClient } from "react-query";
import { refreshUser } from "../../api/auth";
import { getDebitLastMonth } from "../../api/charts";

export const useDebit = () => {
	const queryClient = useQueryClient();

	const { data, isLoading, isSuccess, isError, error, refetch } = useQuery({
		queryKey: ["debit_last_month"],
		queryFn: () => getDebitLastMonth(),
		select: data => data.data,
		retry: false,
		onError: async error => {
			if (error.status === 401) {
				try {
					await refreshUser();
					queryClient.invalidateQueries(["debit_last_month"]);
				} catch {
					window.location.href = "/auth";
				}
			}
		},
	});

	return {
		debitData: data,
		debitIsLoading: isLoading,
		debitIsSuccess: isSuccess,
		debitIsError: isError,
		debitError: error,
		debitRefetch: refetch,
	};
};
