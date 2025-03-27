<script>
	// Add any necessary script logic here
	function toggleAccordion(event) {
		const section = event.target.closest('section');
		if (section) {
			section.classList.toggle('collapsed');
		}
	}
</script>

<style>
	/* General styles */
	body {
		font-family: 'Roboto', sans-serif;
		line-height: 1.8;
		color: #2c3e50;
		background-color: #ecf0f1;
		margin: 0;
		padding: 0;
	}

	main {
		max-width: 900px;
		margin: 2rem auto;
		padding: 2rem;
		background: #ffffff;
		border-radius: 10px;
		box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
	}

	h1 {
		text-align: center;
		color: #2980b9;
		margin-bottom: 2rem;
		font-size: 2rem;
	}

	section {
		margin-bottom: 2rem;
	}

	h2 {
		color: #34495e;
		background: #bdc3c7;
		padding: 0.8rem 1rem;
		border-radius: 5px;
		cursor: pointer;
		user-select: none;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}

	h2:hover {
		background: #95a5a6;
	}

	h2::after {
		content: '▼';
		font-size: 1rem;
		color: #34495e;
		transition: transform 0.3s;
	}

	section.collapsed h2::after {
		transform: rotate(-90deg);
	}

	article {
		margin-bottom: 1.5rem;
		padding: 1rem;
		background: #f8f9fa;
		border: 1px solid #dcdde1;
		border-radius: 5px;
	}

	h3 {
		color: #2c3e50;
		margin-bottom: 0.5rem;
		font-size: 1.2rem;
	}

	p {
		margin: 0.5rem 0;
		color: #7f8c8d;
	}

	ul {
		margin: 0.5rem 0 1rem 1.5rem;
		padding: 0;
		list-style-type: disc;
	}

	li {
		margin-bottom: 0.5rem;
		color: #2c3e50;
	}

	strong {
		color: #2980b9;
	}

	/* Highlight correct answers */
	li strong {
		color: #27ae60;
		font-weight: bold;
	}

	/* Explanation styling */
	p strong {
		color: #34495e;
		font-weight: bold;
	}

	/* Add hover effect for articles */
	article:hover {
		background: #eaf2f8;
		border-color: #2980b9;
		transition: background 0.3s, border-color 0.3s;
	}

	/* Accordion styles */
	section.collapsed > div {
		display: none;
	}
</style>

<main>
	<h1>Anatomy Questions</h1>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 3</h2>
		<div>
			<h3>Chapter 3 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong>What happens to the small and large ribosomal subunits at the end of translation?</strong></p>
				<ul>
						<li>They separate to form DNA.</li>
						<li>They stay together to form amino acids.</li>
						<li>They stay together to form larger molecules.</li>
						<li>They separate and move and are free to join translation of other segments of mRNA.</li>
				</ul>
				<p><strong>Correct Answer:</strong> They separate and move and are free to join translation of other segments of mRNA.</p>
				<p><strong>Explanation:</strong> At the end of translation, the ribosomal subunits disassemble and are reused for translating other mRNA molecules.</p>
			</article>

			<article>
				<h3>Question 2</h3>
				<p><strong>More specifically, on what structure are proteins synthesized?</strong></p>
				<ul>
					<li>RNA</li>
						<li>DNA</li>
						<li>Amino acids</li>
						<li>Ribosomes</li>
				</ul>
				<p><strong>Correct Answer:</strong> Ribosomes</p>
				<p><strong>Explanation:</strong> Ribosomes are the cellular structures where protein synthesis occurs, translating mRNA into polypeptides.</p>
			</article>

			<article>
				<h3>Question 3</h3>
				<p><strong>To whom does the DNA give instructions to build a protein?</strong></p>
				<ul>
					<li>rDNA</li>
						<li>mDNA</li>
						<li>rRNA</li>
						<li>mRNA</li>
				</ul>
				<p><strong>Correct Answer:</strong> mRNA</p>
				<p><strong>Explanation:</strong> DNA provides instructions to mRNA, which carries the genetic code to ribosomes for protein synthesis.</p>
			</article>

			<article>
				<h3>Question 4</h3>
				<p><strong>During what phase of the cell cycle is the DNA replicated?</strong></p>
				<ul>
					<li>G2</li>
					<li>G1</li>
					<li>Cytokinesis</li>
						<li>S</li>
				</ul>
				<p><strong>Correct Answer:</strong> S</p>
				<p><strong>Explanation:</strong> DNA replication occurs during the S (synthesis) phase of the cell cycle.</p>
			</article>

			<article>
				<h3>Question 5</h3>
				<p><strong>Every type of cell goes through mitosis.</strong></p>
				<ul>
						<li>False</li>
					<li>True</li>
				</ul>
				<p><strong>Correct Answer:</strong> False</p>
				<p><strong>Explanation:</strong> Not all cells undergo mitosis. For example, mature red blood cells and neurons do not divide.</p>
			</article>

			<h3>Chapter 3 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong>The diffusion of substances within a solution tends to move those substances ________ their concentration gradient.</strong></p>
				<ul>
					<li>Up</li>
					<li>Down</li>
				</ul>
				<p><strong>Correct Answer:</strong> Down</p>
				<p><strong>Explanation:</strong> Diffusion moves substances from areas of higher concentration to areas of lower concentration, down their concentration gradient.</p>
			</article>

			<article>
				<h3>Question 2</h3>
				<p><strong>Ion pumps and phagocytosis are both examples of ________.</strong></p>
				<ul>
					<li>Endocytosis</li>
					<li>Facilitated transport</li>
					<li>Passive transport</li>
						<li>Active transport</li>
				</ul>
				<p><strong>Correct Answer:</strong> Active transport</p>
				<p><strong>Explanation:</strong> Both ion pumps and phagocytosis require energy (ATP), making them forms of active transport.</p>
			</article>

			<article>
				<h3>Question 3</h3>
				<p><strong>The rough ER has its name due to what associated structures?</strong></p>
				<ul>
					<li>Lysosomes</li>
					<li>Proteins</li>
					<li>Golgi apparatus</li>
						<li>Ribosomes</li>
				</ul>
				<p><strong>Correct Answer:</strong> Ribosomes</p>
				<p><strong>Explanation:</strong> The rough endoplasmic reticulum (ER) is studded with ribosomes, giving it a "rough" appearance.</p>
			</article>

			<article>
				<h3>Question 4</h3>
				<p><strong>Which of the following is a feature common to all three components of the cytoskeleton?</strong></p>
				<ul>
					<li>They all help the cell resist compression and tension.</li>
						<li>They are all polymers of protein subunits.</li>
					<li>They all serve to scaffold the organelles within the cell.</li>
					<li>They are all characterized by roughly the same diameter.</li>
				</ul>
				<p><strong>Correct Answer:</strong> They are all polymers of protein subunits.</p>
				<p><strong>Explanation:</strong> All three components of the cytoskeleton (microfilaments, intermediate filaments, and microtubules) are polymers of protein subunits.</p>
			</article>

			<article>
				<h3>Question 5</h3>
				<p><strong>The nucleus and mitochondria share which of the following features?</strong></p>
				<ul>
					<li>Protein-lined membrane pores</li>
					<li>The production of cellular energy</li>
					<li>The synthesis of ribosomes</li>
						<li>A double cell membrane</li>
				</ul>
				<p><strong>Correct Answer:</strong> A double cell membrane</p>
				<p><strong>Explanation:</strong> Both the nucleus and mitochondria have a double membrane structure.</p>
			</article>

			<article>
				<h3>Question 6</h3>
				<p><strong>Which of the following sequences on a DNA molecule would be complementary to GCTTATAT?</strong></p>
				<ul>
						<li>CGAATATA</li>
					<li>TGCCTCTC</li>
					<li>ATCCGCGC</li>
					<li>TAGGCGCG</li>
				</ul>
				<p><strong>Correct Answer:</strong> CGAATATA</p>
				<p><strong>Explanation:</strong> The complementary sequence to GCTTATAT is CGAATATA.</p>
			</article>

			<article>
				<h3>Question 7</h3>
				<p><strong>Which of the following phases is characterized by preparation for DNA synthesis?</strong></p>
				<ul>
					<li>G0</li>
					<li>S</li>
						<li>G1</li>
					<li>Interphase</li>
				</ul>
				<p><strong>Correct Answer:</strong> G1</p>
				<p><strong>Explanation:</strong> The G1 phase is the phase of the cell cycle where the cell prepares for DNA synthesis.</p>
			</article>

			<article>
				<h3>Question 8</h3>
				<p><strong>How many “letters” of an RNA molecule, in sequence, does it take to provide the code for a single amino acid?</strong></p>
				<ul>
						<li>3</li>
					<li>1</li>
					<li>4</li>
					<li>2</li>
				</ul>
				<p><strong>Correct Answer:</strong> 3</p>
				<p><strong>Explanation:</strong> It takes three nucleotides (a codon) to code for a single amino acid.</p>
			</article>

			<article>
				<h3>Question 9</h3>
				<p><strong>Which of the following are not one of the main types of RNA involved in protein synthesis?</strong></p>
				<ul>
					<li>tRNA</li>
					<li>mRNA</li>
					<li>rRNA</li>
						<li>fRNA</li>
				</ul>
				<p><strong>Correct Answer:</strong> fRNA</p>
				<p><strong>Explanation:</strong> The main types of RNA involved in protein synthesis are tRNA, mRNA, and rRNA. fRNA is not one of them.</p>
			</article>

			<article>
				<h3>Question 10</h3>
				<p><strong>Which of the following is part of the elongation step of DNA synthesis?</strong></p>
				<ul>
					<li>Untwisting the DNA helix</li>
					<li>Pulling apart the two DNA strands</li>
					<li>None of these answers</li>
						<li>Attaching complementary nucleotides to the template strand</li>
				</ul>
				<p><strong>Correct Answer:</strong> Attaching complementary nucleotides to the template strand</p>
				<p><strong>Explanation:</strong> During elongation, complementary nucleotides are attached to the template strand.</p>
			</article>

			<article>
				<h3>Question 11</h3>
				<p><strong>Place the following structures in order from least to most complex organization: chromatin, nucleosome, DNA, chromosome</strong></p>
				<ul>
						<li>DNA, nucleosome, chromatin, chromosome</li>
					<li>Nucleosome, chromatin, DNA, chromosome</li>
					<li>Nucleosome, DNA, chromosome, chromatin</li>
					<li>DNA, chromatin, nucleosome, chromosome</li>
				</ul>
				<p><strong>Correct Answer:</strong> DNA, nucleosome, chromatin, chromosome</p>
				<p><strong>Explanation:</strong> The correct order from least to most complex is DNA, nucleosome, chromatin, chromosome.</p>
			</article>

			<article>
				<h3>Question 12</h3>
				<p><strong>What type of diffusion is of a substance with the aid of a membrane protein?</strong></p>
				<ul>
					<li>ATP diffusion</li>
					<li>Simple diffusion</li>
					<li>Enunciated diffusion</li>
						<li>Facilitated diffusion</li>
				</ul>
				<p><strong>Correct Answer:</strong> Facilitated diffusion</p>
				<p><strong>Explanation:</strong> Facilitated diffusion involves the use of membrane proteins to transport substances across the cell membrane.</p>
			</article>

			<article>
				<h3>Question 13</h3>
				<p><strong>What multipotent stem cells from children are sometimes banked by parents?</strong></p>
				<ul>
					<li>Embryonic stem cells</li>
						<li>Cells from the umbilical cord and from baby teeth</li>
					<li>Hematopoietic stem cells from red and white blood cells</li>
					<li>Fetal stem cells</li>
				</ul>
				<p><strong>Correct Answer:</strong> Cells from the umbilical cord and from baby teeth</p>
				<p><strong>Explanation:</strong> Parents sometimes bank multipotent stem cells from the umbilical cord and baby teeth for potential future medical use.</p>
			</article>

			<article>
				<h3>Question 14</h3>
				<p><strong>Arrange the following terms in order of increasing specialization: oligopotency, pleuripotency, unipotency, multipotency.</strong></p>
				<ul>
					<li>Oligopotency, pleuripotency, unipotency, multipotency</li>
					<li>Multipotency, pleuripotency, oligopotency, unipotency</li>
						<li>Pleuripotency, multipotency, oligopotency, unipotency</li>
					<li>Pleuripotency, oligopotency, multipotency, unipotency</li>
				</ul>
				<p><strong>Correct Answer:</strong> Pleuripotency, multipotency, oligopotency, unipotency</p>
				<p><strong>Explanation:</strong> The correct order of increasing specialization is pleuripotency, multipotency, oligopotency, unipotency.</p>
			</article>

			<article>
				<h3>Question 15</h3>
				<p><strong>Which of the following is not a difference between DNA and RNA?</strong></p>
				<ul>
					<li>DNA contains thymine whereas RNA contains uracil</li>
					<li>RNA is single stranded and DNA is double stranded</li>
						<li>DNA contains alternating sugar-phosphate molecules whereas RNA does not contain sugars</li>
					<li>DNA contains deoxyribose and RNA contains ribose</li>
				</ul>
				<p><strong>Correct Answer:</strong> DNA contains alternating sugar-phosphate molecules whereas RNA does not contain sugars</p>
				<p><strong>Explanation:</strong> Both DNA and RNA contain alternating sugar-phosphate molecules. The other options are true differences between DNA and RNA.</p>
			</article>

			<article>
				<h3>Question 16</h3>
				<p><strong>What is the third stage of mitosis (and meiosis), during which sister chromatids separate into two new nuclear regions of a dividing cell?</strong></p>
				<ul>
					<li>Metaphase</li>
					<li>Prophase</li>
						<li>Anaphase</li>
					<li>Telophase</li>
				</ul>
				<p><strong>Correct Answer:</strong> Anaphase</p>
				<p><strong>Explanation:</strong> Anaphase is the third stage of mitosis and meiosis, where sister chromatids separate.</p>
			</article>

			<article>
				<h3>Question 17</h3>
				<p><strong>What is the term used to describe the “skeleton” of a cell that is formed by rod-like proteins that support the cell’s shape and provide, among other functions, locomotive abilities?</strong></p>
				<ul>
						<li>Cytoskeleton</li>
					<li>Cytoplasm</li>
					<li>Nuclear envelope</li>
					<li>Cytosol</li>
				</ul>
				<p><strong>Correct Answer:</strong> Cytoskeleton</p>
				<p><strong>Explanation:</strong> The cytoskeleton is the network of rod-like proteins that support the cell's shape and provide locomotive abilities.</p>
			</article>

			<article>
				<h3>Question 18</h3>
				<p><strong>What term describes the condition of being committed to a single specialized cell type?</strong></p>
				<ul>
					<li>Multiplotent</li>
						<li>Unipotent</li>
					<li>Pluripotent</li>
					<li>Totipotent</li>
				</ul>
				<p><strong>Correct Answer:</strong> Unipotent</p>
				<p><strong>Explanation:</strong> Unipotent cells are committed to a single specialized cell type.</p>
			</article>

			<article>
				<h3>Question 19</h3>
				<p><strong>Which of the following organelles produces large quantities of ATP when both glucose and oxygen are available to the cell?</strong></p>
				<ul>
						<li>Mitochondria</li>
					<li>Lysosomes</li>
					<li>Endoplasmic reticulum</li>
					<li>Peroxisomes</li>
				</ul>
				<p><strong>Correct Answer:</strong> Mitochondria</p>
				<p><strong>Explanation:</strong> Mitochondria are the organelles responsible for producing large quantities of ATP when glucose and oxygen are available.</p>
			</article>

			<article>
				<h3>Question 20</h3>
				<p><strong>Which cellular organelle functions in protein synthesis?</strong></p>
				<ul>
					<li>Golgi apparatus</li>
					<li>Nucleus</li>
						<li>Ribosome</li>
					<li>Smooth ER</li>
				</ul>
				<p><strong>Correct Answer:</strong> Ribosome</p>
				<p><strong>Explanation:</strong> Ribosomes are the cellular organelles that function in protein synthesis.</p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 4 - Tissue Level</h2>
		<div>
			<h3>Chapter 4 - Homework</h3>
         
			<h3>Chapter 4 - Quiz</h3>
            
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 5 - Integumentary System</h2>
		<div>
			<h3>Chapter 5 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<article>
				<h3>Question 2</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 5 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<article>
				<h3>Question 2</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 6 - Bone Tissue and the Skeletal System</h2>
		<div>
			<h3>Chapter 6 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 6 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 9 - Joints</h2>
		<div>
			<h3>Chapter 9 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 9 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 10 - Muscle Tissue</h2>
		<div>
			<h3>Chapter 10 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 10 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 11 - Muscular System</h2>
		<div>
			<h3>Chapter 11 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 11 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 12 - Nervous System and Nervous Tissue</h2>
		<div>
			<h3>Chapter 12 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 12 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 17 - Endocrine System</h2>
		<div>
			<h3>Chapter 17 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 17 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 19 - The Heart</h2>
		<div>
			<h3>Chapter 19 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 19 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 21 - Lymphatic and Immune System</h2>
		<div>
			<h3>Chapter 21 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 21 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 22 - Respiratory System</h2>
		<div>
			<h3>Chapter 22 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 22 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 23 - Digestive System</h2>
		<div>
			<h3>Chapter 23 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong>The first place your food will go is the oral cavity.</strong></p>
				<ul>
					<li>True</li>
					<li>False</li>
				</ul>
				<p><strong>Correct Answer:</strong> True</p>
				<p><strong>Explanation:</strong> The oral cavity (mouth) is the first part of the digestive system where food enters. It is where mechanical digestion (chewing) and chemical digestion (saliva breaking down carbohydrates) begin.</p>
			</article>

			<article>
				<h3>Question 2</h3>
				<p><strong>Chewing is the enzymatic breakdown of food.</strong></p>
				<ul>
					<li>True</li>
					<li>False</li>
				</ul>
				<p><strong>Correct Answer:</strong> False</p>
				<p><strong>Explanation:</strong> Chewing is a mechanical process, not enzymatic. It physically breaks food into smaller pieces to increase the surface area for enzymes in saliva to act on.</p>
			</article>

			<article>
				<h3>Question 3</h3>
				<p><strong>A bolus is a sphere of digested food.</strong></p>
				<ul>
					<li>True</li>
					<li>False</li>
				</ul>
				<p><strong>Correct Answer:</strong> True</p>
				<p><strong>Explanation:</strong> A bolus is a soft, rounded mass of chewed food mixed with saliva, formed in the mouth and ready to be swallowed. It is not fully digested but is prepared for further digestion in the stomach.</p>
			</article>

			<article>
				<h3>Question 4</h3>
				<p><strong>Chyme is a more digested bolus that then moves into the esophagus.</strong></p>
				<ul>
					<li>True</li>
					<li>False</li>
				</ul>
				<p><strong>Correct Answer:</strong> False</p>
				<p><strong>Explanation:</strong> Chyme is a semi-liquid mixture of partially digested food and digestive juices formed in the stomach. It does not move into the esophagus; instead, it moves into the small intestine for further digestion and absorption.</p>
			</article>

			<article>
				<h3>Question 5</h3>
				<p><strong>In the colon, there is a lot of digestion that occurs.</strong></p>
				<ul>
					<li>True</li>
					<li>False</li>
				</ul>
				<p><strong>Correct Answer:</strong> False</p>
				<p><strong>Explanation:</strong> The colon (large intestine) is primarily responsible for absorbing water and electrolytes, not digestion. Most digestion occurs in the stomach and small intestine. The colon mainly processes waste and prepares it for elimination.</p>
			</article>

			<h3>Chapter 23 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong>Which of the following membranes covers the stomach?</strong></p>
				<ul>
					<li>Parietal peritoneum</li>
					<li>Falciform ligament</li>
					<li>Mesocolon</li>
						<li>Visceral peritoneum</li>
				</ul>
				<p><strong>Correct Answer:</strong> Visceral peritoneum</p>
				<p><strong>Explanation:</strong> The visceral peritoneum is the membrane that directly covers the stomach and other abdominal organs.</p>
			</article>

			<article>
				<h3>Question 2</h3>
				<p><strong>The ____________________ system benefits the digestive system by ______________________________________________.</strong></p>
				<ul>
					<li>Nervous, Respiratory organs that provide oxygen and remove carbon dioxide</li>
					<li>Integumentary, Sensory and motor neurons that help regulate secretions and muscle contractions in the digestive tract</li>
					<li>Lymphatic, Endocrine hormones that help regulate secretion in digestive glands and accessory organs</li>
						<li>Nervous, Sensory and motor neurons that help regulate secretions and muscle contractions in the digestive tract</li>
				</ul>
				<p><strong>Correct Answer:</strong> Nervous, Sensory and motor neurons that help regulate secretions and muscle contractions in the digestive tract</p>
				<p><strong>Explanation:</strong> The nervous system plays a key role in regulating digestive processes through sensory and motor neurons.</p>
			</article>

			<article>
				<h3>Question 3</h3>
				<p><strong>The _________________ is the final segment of the large intestine.</strong></p>
				<ul>
					<li>Jejunum</li>
					<li>Anal sinus</li>
					<li>Anal column</li>
						<li>Anal canal</li>
				</ul>
				<p><strong>Correct Answer:</strong> Anal canal</p>
				<p><strong>Explanation:</strong> The anal canal is the terminal part of the large intestine, leading to the anus for waste elimination.</p>
			</article>

			<article>
				<h3>Question 4</h3>
				<p><strong>Which of these nutrients is absorbed mainly in the duodenum?</strong></p>
				<ul>
					<li>Water</li>
					<li>Glucose</li>
					<li>Sodium</li>
						<li>Iron</li>
				</ul>
				<p><strong>Correct Answer:</strong> Iron</p>
				<p><strong>Explanation:</strong> Iron is primarily absorbed in the duodenum, the first part of the small intestine.</p>
			</article>

			<article>
				<h3>Question 5</h3>
				<p><strong>Which of these is involved in the chemical digestion of protein?</strong></p>
				<ul>
					<li>Sucrase</li>
					<li>Pancreatic nuclease</li>
					<li>Pancreatic amylase</li>
						<li>Trypsin</li>
				</ul>
				<p><strong>Correct Answer:</strong> Trypsin</p>
				<p><strong>Explanation:</strong> Trypsin is an enzyme involved in the chemical digestion of proteins in the small intestine.</p>
			</article>

			<article>
				<h3>Question 6</h3>
				<p><strong>Where does the chemical digestion of starch begin?</strong></p>
				<ul>
					<li>Small intestine</li>
						<li>Mouth</li>
					<li>Esophagus</li>
					<li>Stomach</li>
				</ul>
				<p><strong>Correct Answer:</strong> Mouth</p>
				<p><strong>Explanation:</strong> The chemical digestion of starch begins in the mouth with the enzyme amylase in saliva.</p>
			</article>

			<article>
				<h3>Question 7</h3>
				<p><strong>Where are most fat-digesting enzymes produced?</strong></p>
				<ul>
					<li>Gallbladder</li>
						<li>Pancreas</li>
					<li>Large intestine</li>
					<li>Liver</li>
				</ul>
				<p><strong>Correct Answer:</strong> Pancreas</p>
				<p><strong>Explanation:</strong> The pancreas produces most of the enzymes involved in fat digestion.</p>
			</article>

			<article>
				<h3>Question 8</h3>
				<p><strong>During gastric emptying, chyme is released into the duodenum through the ________.</strong></p>
				<ul>
					<li>Pyloric antrum</li>
					<li>Pyloric canal</li>
					<li>Esophageal hiatus</li>
						<li>Pyloric sphincter</li>
				</ul>
				<p><strong>Correct Answer:</strong> Pyloric sphincter</p>
				<p><strong>Explanation:</strong> The pyloric sphincter regulates the release of chyme from the stomach into the duodenum.</p>
			</article>

			<article>
				<h3>Question 9</h3>
				<p><strong>Which of these statements about the pharynx is true?</strong></p>
				<ul>
					<li>The nasopharynx is involved in digestion.</li>
						<li>The oropharynx begins inferior to the nasopharynx and is continuous below with the laryngopharynx.</li>
					<li>It extends from the nasal and oral cavities superiorly to the esophagus anteriorly.</li>
					<li>The laryngopharynx is composed partially of cartilage.</li>
				</ul>
				<p><strong>Correct Answer:</strong> The oropharynx begins inferior to the nasopharynx and is continuous below with the laryngopharynx.</p>
				<p><strong>Explanation:</strong> The oropharynx is the part of the pharynx that begins below the nasopharynx and continues with the laryngopharynx.</p>
			</article>

			<article>
				<h3>Question 10</h3>
				<p><strong>Which structure is located where the esophagus penetrates the diaphragm?</strong></p>
				<ul>
					<li>Upper esophageal sphincter</li>
					<li>Cardiac orifice</li>
					<li>Lower esophageal sphincter</li>
						<li>Esophageal hiatus</li>
				</ul>
				<p><strong>Correct Answer:</strong> Esophageal hiatus</p>
				<p><strong>Explanation:</strong> The esophageal hiatus is the opening in the diaphragm through which the esophagus passes.</p>
			</article>

			<article>
				<h3>Question 11</h3>
				<p><strong>Which phase of deglutition involves contraction of the longitudinal muscle layer of the muscularis?</strong></p>
				<ul>
					<li>Buccal phase</li>
						<li>Esophageal phase</li>
					<li>Pharyngeal phase</li>
					<li>Voluntary phase</li>
				</ul>
				<p><strong>Correct Answer:</strong> Esophageal phase</p>
				<p><strong>Explanation:</strong> The esophageal phase of deglutition involves the contraction of the longitudinal muscle layer of the muscularis to move the bolus down the esophagus.</p>
			</article>

			<article>
				<h3>Question 12</h3>
				<p><strong>Which of these organs is not considered an accessory digestive structure?</strong></p>
				<ul>
					<li>Pancreas</li>
						<li>Mouth</li>
					<li>Liver</li>
					<li>Salivary glands</li>
				</ul>
				<p><strong>Correct Answer:</strong> Mouth</p>
				<p><strong>Explanation:</strong> The mouth is part of the main digestive tract, not an accessory structure.</p>
			</article>

			<article>
				<h3>Question 13</h3>
				<p><strong>Which of these cells secrete hormones?</strong></p>
				<ul>
					<li>Chief cells</li>
						<li>Enteroendocrine cells</li>
					<li>Parietal cells</li>
					<li>Mucous neck cells</li>
				</ul>
				<p><strong>Correct Answer:</strong> Enteroendocrine cells</p>
				<p><strong>Explanation:</strong> Enteroendocrine cells secrete hormones that regulate various functions of the digestive system.</p>
			</article>

			<article>
				<h3>Question 14</h3>
				<p><strong>Parietal cells secrete ________.</strong></p>
				<ul>
					<li>Pepsinogen</li>
						<li>Hydrochloric acid</li>
					<li>Pepsin</li>
					<li>Gastrin</li>
				</ul>
				<p><strong>Correct Answer:</strong> Hydrochloric acid</p>
				<p><strong>Explanation:</strong> Parietal cells in the stomach secrete hydrochloric acid, which helps in digestion.</p>
			</article>

			<article>
				<h3>Question 15</h3>
				<p><strong>Which of these is most associated with villi?</strong></p>
				<ul>
					<li>Haustra</li>
					<li>Bacterial flora</li>
					<li>Intestinal glands</li>
						<li>Lacteals</li>
				</ul>
				<p><strong>Correct Answer:</strong> Lacteals</p>
				<p><strong>Explanation:</strong> Lacteals are lymphatic vessels found in the villi of the small intestine, involved in the absorption of fats.</p>
			</article>

			<article>
				<h3>Question 16</h3>
				<p><strong>What is the role of the small intestine’s MALT?</strong></p>
				<ul>
					<li>Secreting mucus</li>
					<li>Buffering acidic chyme</li>
						<li>Preventing bacteria from entering the bloodstream</li>
					<li>Activating pepsin</li>
				</ul>
				<p><strong>Correct Answer:</strong> Preventing bacteria from entering the bloodstream</p>
				<p><strong>Explanation:</strong> Mucosa-associated lymphoid tissue (MALT) in the small intestine helps prevent bacteria from entering the bloodstream.</p>
			</article>

			<article>
				<h3>Question 17</h3>
				<p><strong>Which of these processes occurs throughout most of the alimentary canal?</strong></p>
				<ul>
						<li>Propulsion</li>
					<li>Absorption</li>
					<li>Segmentation</li>
					<li>Ingestion</li>
				</ul>
				<p><strong>Correct Answer:</strong> Propulsion</p>
				<p><strong>Explanation:</strong> Propulsion, the movement of food through the digestive tract, occurs throughout most of the alimentary canal.</p>
			</article>

			<article>
				<h3>Question 18</h3>
				<p><strong>Which part of the large intestine attaches to the appendix?</strong></p>
				<ul>
					<li>Descending colon</li>
					<li>Transverse colon</li>
						<li>Cecum</li>
					<li>Ascending colon</li>
				</ul>
				<p><strong>Correct Answer:</strong> Cecum</p>
				<p><strong>Explanation:</strong> The appendix is attached to the cecum, the first part of the large intestine.</p>
			</article>

			<article>
				<h3>Question 19</h3>
				<p><strong>Pancreatic juice ________.</strong></p>
				<ul>
					<li>Is secreted by pancreatic islet cells</li>
						<li>Buffers chyme</li>
					<li>Is released into the cystic duct</li>
					<li>Deactivates bile</li>
				</ul>
				<p><strong>Correct Answer:</strong> Buffers chyme</p>
				<p><strong>Explanation:</strong> Pancreatic juice contains bicarbonate, which helps buffer the acidic chyme entering the small intestine from the stomach.</p>
			</article>

			<article>
				<h3>Question 20</h3>
				<p><strong>The ________________________________ is the midline mucous membrane fold that attaches the inner surface of the lips to the gums.</strong></p>
				<ul>
						<li>Labial frenulum</li>
					<li>Nucleosidase</li>
					<li>Laryngopharynx</li>
					<li>Micelle</li>
				</ul>
				<p><strong>Correct Answer:</strong> Labial frenulum</p>
				<p><strong>Explanation:</strong> The labial frenulum is the fold of mucous membrane that attaches the inner surface of the lips to the gums.</p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 25 - Urinary System</h2>
		<div>
			<h3>Chapter 25 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 25 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 27 - Reproductive System</h2>
		<div>
			<h3>Chapter 27 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 27 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 28 - Development and Inheritance</h2>
		<div>
			<h3>Chapter 28 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 28 - Quiz</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong></strong></p>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
				</ul>
				<p><strong>Correct Answer:</strong></p>
				<p><strong>Explanation:</strong></p>
			</article>
		</div>
	</section>
</main>