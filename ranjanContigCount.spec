/*
   A KBase module: ranjanContigCount
 */

module ranjanContigCount {
	/*
	   Insert your typespec information here.
	 */

	typedef string contigset_id;
	typedef structure {
		int contig_count;
	} CountContigResults;


	funcdef count_contigs (string workspace_name, contigset_id contigset)
		returns (CountContigResults) authentication required;

};
