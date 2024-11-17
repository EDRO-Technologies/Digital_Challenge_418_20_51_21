import { useQuery } from "react-query";
import { logoutUser } from "../../api/auth.js";

export const useLogout = () => {
	const { data, isLoading, isSuccess, isError, error, refetch } = useQuery({
		queryKey: ["logout"],
		queryFn: () => logoutUser(),
		select: data => data.data,
		retry: false,
		enabled: false,
		onSuccess: () => {
			window.location.href = "/auth";
		},
	});

	return {
		logoutData: data,
		logoutIsLoading: isLoading,
		logoutIsSuccess: isSuccess,
		logoutIsError: isError,
		logoutError: error,
		logoutRefetch: refetch,
	};
};
