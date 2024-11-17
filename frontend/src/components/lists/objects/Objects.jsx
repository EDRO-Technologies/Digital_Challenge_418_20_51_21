import { Listbox, ListboxItem } from "@nextui-org/listbox";
import ListboxWrapper from "./ListboxWrapper";

const Objects = ({ objects, handleButtonClick }) => {
	return (
		<div className="border-small rounded-md border-solid border-[#e5e5e5] h-72">
			<ListboxWrapper>
				<Listbox
					aria-label="Listbox Variants"
					color="default"
					variant="flat"
					classNames={{
						list: "max-h-64 overflow-scroll",
					}}
				>
					{objects.map((obj, i) => (
						<ListboxItem key={i} onClick={() => handleButtonClick(obj.coord)}>
							{obj.name}
						</ListboxItem>
					))}
				</Listbox>
			</ListboxWrapper>
		</div>
	);
};

export default Objects;
