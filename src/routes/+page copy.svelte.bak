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
			<article>
				<h3>Question 1</h3>
				<p><strong>What is the primary function of epithelial tissue?</strong></p>
				<ul>
					<li>Support and structure</li>
					<li>Protection and secretion</li>
					<li>Movement</li>
					<li>Energy storage</li>
				</ul>
				<p><strong>Correct Answer:</strong> Protection and secretion</p>
				<p><strong>Explanation:</strong> Epithelial tissue covers body surfaces and lines cavities, providing protection and facilitating secretion.</p>
			</article>
         
			<h3>Chapter 4 - Quiz</h3>
            
		</div>
	</section>

	<section class="collapsed">
		<h2 on:click={toggleAccordion}>Chapter 5 - Integumentary System</h2>
		<div>
			<h3>Chapter 5 - Homework</h3>
			<article>
				<h3>Question 1</h3>
				<p><strong>What is the primary function of the skin?</strong></p>
				<ul>
					<li>Regulating blood pressure</li>
					<li>Protection against environmental hazards</li>
					<li>Producing red blood cells</li>
					<li>Storing calcium</li>
				</ul>
				<p><strong>Correct Answer:</strong> Protection against environmental hazards</p>
				<p><strong>Explanation:</strong> The skin acts as a barrier to protect the body from environmental hazards such as pathogens, UV radiation, and dehydration.</p>
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
				<p><strong>What is the primary function of osteoblasts?</strong></p>
				<ul>
					<li>Breaking down bone tissue</li>
					<li>Producing red blood cells</li>
					<li>Building new bone tissue</li>
					<li>Storing calcium</li>
				</ul>
				<p><strong>Correct Answer:</strong> Building new bone tissue</p>
				<p><strong>Explanation:</strong> Osteoblasts are cells responsible for forming new bone tissue by producing the bone matrix.</p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Doctors can not determine one's growth rate.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>All bones have the same growth rate.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>Skeletal maturity is reached at about the ages of 14 for girls and 16 for boys.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>Limb length discrepancies can affect your mobility.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 6 - Quiz</h3>
			<article>
                <h3>Question 1</h3>
                <p><strong>Which function of the skeletal system would be especially important if you were in a car accident?</strong></p>
                <ul>
                  <li>fat storage</li>
                  <li>storage of minerals</li>
                  <li>protection of internal organs</li>
                  <li>facilitation of movement</li>
                </ul>
                <p><strong>Correct Answer:</strong> protection of internal organs</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Bone tissue can be described as _________ .</strong></p>
                <ul>
                  <li>cartilage</li>
                  <li>the skeletal system</li>
                  <li>dead calcified tissue</li>
                  <li>dense, hard connective tissue</li>
                </ul>
                <p><strong>Correct Answer:</strong> dense, hard connective tissue</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>Without red marrow, bones would not be able to ________.</strong></p>
                <ul>
                  <li>move like levers</li>
                  <li>store calcium</li>
                  <li>make blood cells</li>
                  <li>store phosphate</li>
                </ul>
                <p><strong>Correct Answer:</strong> make blood cells</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>Yellow marrow has been identified as ________.</strong></p>
                <ul>
                  <li>the hard portion of bone</li>
                  <li>a point of attachment for muscles</li>
                  <li>an area of fat storage</li>
                  <li>the cause of kyphosis</li>
                </ul>
                <p><strong>Correct Answer:</strong> an area of fat storage</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>The skeletal system is made of ________.</strong></p>
                <ul>
                  <li>bones and cartilage</li>
                  <li>muscles and tendons</li>
                  <li>vitreous humor</li>
                  <li>minerals and fat</li>
                </ul>
                <p><strong>Correct Answer:</strong> bones and cartilage</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 6</h3>
                <p><strong>With respect to their direct effects on osseous tissue, which pair of hormones has actions that oppose each other?</strong></p>
                <ul>
                  <li>estrogen and testosterone</li>
                  <li>calcitonin and parathyroid hormone</li>
                  <li>estrogen and progesterone</li>
                  <li>calcitonin and calcitriol</li>
                </ul>
                <p><strong>Correct Answer:</strong> calcitonin and parathyroid hormone</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 7</h3>
                <p><strong>Most of the bones of the arms and hands are long bones; however, the bones in the wrist are categorized as ________.</strong></p>
                <ul>
                  <li>sesamoid bones</li>
                  <li>short bones</li>
                  <li>irregular bones</li>
                  <li>flat bones</li>
                </ul>
                <p><strong>Correct Answer:</strong> short bones</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 8</h3>
                <p><strong>Sesamoid bones are found embedded in ________.</strong></p>
                <ul>
                  <li>muscles</li>
                  <li>tendons</li>
                  <li>joints</li>
                  <li>ligaments</li>
                </ul>
                <p><strong>Correct Answer:</strong> tendons</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 9</h3>
                <p><strong>Bones that surround the spinal cord are classified as ________ bones.</strong></p>
                <ul>
                  <li>flat</li>
                  <li>irregular</li>
                  <li>short</li>
                  <li>sesamoid</li>
                </ul>
                <p><strong>Correct Answer:</strong> irregular</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 10</h3>
                <p><strong>Which category of bone is among the most numerous in the skeleton?</strong></p>
                <ul>
                  <li>flat bone</li>
                  <li>long bone</li>
                  <li>sesamoid bone</li>
                  <li>short bone</li>
                </ul>
                <p><strong>Correct Answer:</strong> long bone</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 11</h3>
                <p><strong>All of the following play a role in calcium homeostasis except:</strong></p>
                <ul>
                  <li>calcitonin</li>
                  <li>thyroxine</li>
                  <li>parathyroid hormone</li>
                  <li>vitamin D</li>
                </ul>
                <p><strong>Correct Answer:</strong> thyroxine</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 12</h3>
                <p><strong>Which of the following occurs in the spongy bone of the epiphysis?</strong></p>
                <ul>
                  <li>bone remodeling</li>
                  <li>shock absorption</li>
                  <li>hematopoiesis</li>
                  <li>bone growth</li>
                </ul>
                <p><strong>Correct Answer:</strong> hematopoiesis</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 13</h3>
                <p><strong>The fibrous membrane covering the outer surface of the bone is the ________.</strong></p>
                <ul>
                  <li>periosteum</li>
                  <li>diaphysis</li>
                  <li>endosteum</li>
                  <li>epiphysis</li>
                </ul>
                <p><strong>Correct Answer:</strong> periosteum</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 14</h3>
                <p><strong>What type of fracture has several breaks that result in many small pieces between two large segments?</strong></p>
                <ul>
                  <li>Comminuted</li>
                  <li>Transverse</li>
                  <li>Greenstick</li>
                  <li>Spiral</li>
                </ul>
                <p><strong>Correct Answer:</strong> Comminuted</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 15</h3>
                <p><strong>Which of the following are found in compact bone and cancellous bone?</strong></p>
                <ul>
                  <li>Haversian canals</li>
                  <li>Haversian systems</li>
                  <li>bone marrow</li>
                  <li>lamellae</li>
                </ul>
                <p><strong>Correct Answer:</strong> lamellae</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 16</h3>
                <p><strong>The area of a bone where the nutrient foramen passes forms what kind of bone marking?</strong></p>
                <ul>
                  <li>a fissure</li>
                  <li>a facet</li>
                  <li>a hole</li>
                  <li>a canal</li>
                </ul>
                <p><strong>Correct Answer:</strong> a hole</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 17</h3>
                <p><strong>Bones grow in length due to activity in the ________.</strong></p>
                <ul>
                  <li>medullary cavity</li>
                  <li>epiphyseal plate</li>
                  <li>perichondrium</li>
                  <li>periosteum</li>
                </ul>
                <p><strong>Correct Answer:</strong> epiphyseal plate</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 18</h3>
                <p><strong>Which of the following is most likely to be released when blood calcium levels are elevated?</strong></p>
                <ul>
                  <li>vitamin D</li>
                  <li>calcitonin</li>
                  <li>thyroxine</li>
                  <li>parathyroid hormone</li>
                </ul>
                <p><strong>Correct Answer:</strong> calcitonin</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 19</h3>
                <p><strong>Which one of the following foods is best for bone health?</strong></p>
                <ul>
                  <li>liver</li>
                  <li>leafy green vegetables</li>
                  <li>oranges</li>
                  <li>carrots</li>
                </ul>
                <p><strong>Correct Answer:</strong> leafy green vegetables</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 20</h3>
                <p><strong>Which of the following contain channels within the bone matrix that house one of an osteocyte’s many cytoplasmic extensions that it uses to communicate and receive nutrients?</strong></p>
                <ul>
                  <li>diploë</li>
                  <li>cartilage</li>
                  <li>compact bone</li>
                  <li>canaliculi</li>
                </ul>
                <p><strong>Correct Answer:</strong> canaliculi</p>
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
                <p><strong>The hip joint includes the ball shaped head of the femur.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>The most common cause of hip disability is osteoarthritis.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>The prosthetic hip joint is put into place using glue.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>A new prosthetic hip will last about 15-20 years.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>The new hip joint will fit into the femur.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 9 - Quiz</h3>
			<article>
                <h3>Question 1</h3>
                <p><strong>Which of these joints is classified as a synarthrosis?</strong></p>
                <ul>
                  <li>the pubic symphysis</li>
                  <li>an invertebral disc</li>
                  <li>the shoulder joint</li>
                  <li>the manubriosternal joint</li>
                </ul>
                <p><strong>Correct Answer:</strong> the manubriosternal joint</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Which of these joints is classified as a biaxial diarthrosis?</strong></p>
                <ul>
                  <li>the hip joint</li>
                  <li>the elbow joint</li>
                  <li>the pubic symphysis</li>
                  <li>the metacarpophalangeal joint</li>
                </ul>
                <p><strong>Correct Answer:</strong> the metacarpophalangeal joint</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>Intramembranous ossification ________.</strong></p>
                <ul>
                  <li>produces the bones of the top and sides of the skull</li>
                  <li>involves the conversion of a hyaline cartilage model into bone</li>
                  <li>gives rise to the bones of the limbs</li>
                  <li>produces the bones of the face and base of the skull</li>
                </ul>
                <p><strong>Correct Answer:</strong> produces the bones of the top and sides of the skull</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>Which type of fibrous joint connects the tibia and fibula?</strong></p>
                <ul>
                  <li>symphysis</li>
                  <li>syndesmosis</li>
                  <li>suture</li>
                  <li>gomphosis</li>
                </ul>
                <p><strong>Correct Answer:</strong> syndesmosis</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>An example of a wide fibrous joint is ________.</strong></p>
                <ul>
                  <li>a synostosis</li>
                  <li>a suture joint</li>
                  <li>the interosseous membrane of the forearm</li>
                  <li>a gomphosis</li>
                </ul>
                <p><strong>Correct Answer:</strong> the interosseous membrane of the forearm</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 6</h3>
                <p><strong>A cartilaginous joint ________.</strong></p>
                <ul>
                  <li>is formed by a wide sheet of fibrous connective tissue</li>
                  <li>is called a symphysis when the bones are united by fibrocartilage</li>
                  <li>has a joint cavity</li>
                  <li>anchors the teeth to the jaws</li>
                </ul>
                <p><strong>Correct Answer:</strong> is called a symphysis when the bones are united by fibrocartilage</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 7</h3>
                <p><strong>The epiphyseal plate of a growing long bone in a child is classified as a ________.</strong></p>
                <ul>
                  <li>symphysis</li>
                  <li>synostosis</li>
                  <li>syndesmosis</li>
                  <li>synchondrosis</li>
                </ul>
                <p><strong>Correct Answer:</strong> synchondrosis</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 8</h3>
                <p><strong>Which type of joint provides the greatest range of motion?</strong></p>
                <ul>
                  <li>hinge</li>
                  <li>condyloid</li>
                  <li>ball-and-socket</li>
                  <li>plane</li>
                </ul>
                <p><strong>Correct Answer:</strong> ball-and-socket</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 9</h3>
                <p><strong>Which type of joint allows for only uniaxial movement?</strong></p>
                <ul>
                  <li>hinge joint</li>
                  <li>saddle joint</li>
                  <li>ball-and-socket joint</li>
                  <li>condyloid joint</li>
                </ul>
                <p><strong>Correct Answer:</strong> hinge joint</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 10</h3>
                <p><strong>Endochondral ossification is ________.</strong></p>
                <ul>
                  <li>completed before birth</li>
                  <li>the process that replaces hyaline cartilage with bone tissue</li>
                  <li>the process by which mesenchyme differentiates directly into bone tissue</li>
                  <li>the process that gives rise to the joint interzone and future joint cavity</li>
                </ul>
                <p><strong>Correct Answer:</strong> the process that replaces hyaline cartilage with bone tissue</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 11</h3>
                <p><strong>A bursa ________.</strong></p>
                <ul>
                  <li>prevents friction between skin and bone, or a muscle tendon and bone</li>
                  <li>is the strong band of connective tissue that holds bones together at a synovial joint</li>
                  <li>surrounds a tendon at the point where the tendon crosses a joint</li>
                  <li>secretes the lubricating fluid for a synovial joint</li>
                </ul>
                <p><strong>Correct Answer:</strong> prevents friction between skin and bone, or a muscle tendon and bone</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 12</h3>
                <p><strong>Condyloid joints ________.</strong></p>
                <ul>
                  <li>are a uniaxial diarthrosis joint</li>
                  <li>are found at the proximal radioulnar joint</li>
                  <li>include the radiocarpal joint</li>
                  <li>are a type of ball-and-socket joint</li>
                </ul>
                <p><strong>Correct Answer:</strong> include the radiocarpal joint</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 13</h3>
                <p><strong>A meniscus is ________.</strong></p>
                <ul>
                  <li>a fluid-filled space that prevents friction between a muscle tendon and underlying bone</li>
                  <li>a fibrocartilage pad that provides padding between bones</li>
                  <li>the articular cartilage that covers the ends of a bone at a synovial joint</li>
                  <li>the lubricating fluid within a synovial joint</li>
                </ul>
                <p><strong>Correct Answer:</strong> a fibrocartilage pad that provides padding between bones</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 14</h3>
                <p><strong>Which motion moves the bottom of the foot away from the midline of the body?</strong></p>
                <ul>
                  <li>elevation</li>
                  <li>eversion</li>
                  <li>plantar flexion</li>
                  <li>dorsiflexion</li>
                </ul>
                <p><strong>Correct Answer:</strong> eversion</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 15</h3>
                <p><strong>Supination is the motion that moves the ________.</strong></p>
                <ul>
                  <li>foot so that the bottom of the foot faces the midline of the body</li>
                  <li>hand from the palm backward position to the palm forward position</li>
                  <li>hand from the palm forward position to the palm backward position</li>
                  <li>scapula in an upward direction</li>
                </ul>
                <p><strong>Correct Answer:</strong> hand from the palm backward position to the palm forward position</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 16</h3>
                <p><strong>________________ is the excessive flexion of joint.</strong></p>
                <ul>
                  <li>Pariflexion</li>
                  <li>Hyperflexion</li>
                  <li>Uniflexion</li>
                  <li>Hypoflexion</li>
                </ul>
                <p><strong>Correct Answer:</strong> Hyperflexion</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 17</h3>
                <p><strong>Intramembranous ossification ________.</strong></p>
                <ul>
                  <li>produces the bones of the top and sides of the skull</li>
                  <li>involves the conversion of a hyaline cartilage model into bone</li>
                  <li>gives rise to the bones of the limbs</li>
                  <li>produces the bones of the face and base of the skull</li>
                </ul>
                <p><strong>Correct Answer:</strong> produces the bones of the top and sides of the skull</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 18</h3>
                <p><strong>Which region of the vertebral column has the greatest range of motion for rotation?</strong></p>
                <ul>
                  <li>lumbar</li>
                  <li>cervical</li>
                  <li>thoracic</li>
                  <li>sacral</li>
                </ul>
                <p><strong>Correct Answer:</strong> thoracic</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 19</h3>
                <p><strong>Synovial joints ________.</strong></p>
                <ul>
                  <li>are produced by intramembranous ossification</li>
                  <li>are derived from fontanelles</li>
                  <li>are produced by endochondral ossification</li>
                  <li>develop at an interzone site</li>
                </ul>
                <p><strong>Correct Answer:</strong> develop at an interzone site</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 20</h3>
                <p><strong>A __________________ is a slightly mobile joint.</strong></p>
                <ul>
                  <li>ellipsoidal</li>
                  <li>amphiarthrosis</li>
                  <li>diarthrosis</li>
                  <li>pivot</li>
                </ul>
                <p><strong>Correct Answer:</strong> amphiarthrosis</p>
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
                <p><strong>Skeletal muscle is also known as striated muscle.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Muscle tissue is named for how it reacts to dye under a microscope.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>Skeletal muscle cells are among the smallest in the body.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>Each muscle fiber runs the entire length of the muscle in the body.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>Myosin is also known as "thick filaments".</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 10 - Quiz</h3>
			<article>
                <h3>Question 1</h3>
                <p><strong>Muscle that has a striped appearance is described as being ________.</strong></p>
                <ul>
                  <li>striated</li>
                  <li>nonstriated</li>
                  <li>elastic</li>
                  <li>excitable</li>
                </ul>
                <p><strong>Correct Answer:</strong> striated</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Which of the following properties is not common to all three muscle tissues?</strong></p>
                <ul>
                  <li>at rest, uses shielding proteins to cover actin-binding sites</li>
                  <li>excitability</li>
                  <li>elasticity</li>
                  <li>the need for ATP</li>
                </ul>
                <p><strong>Correct Answer:</strong> at rest, uses shielding proteins to cover actin-binding sites</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>Which of the following statements describes smooth muscle cells?</strong></p>
                <ul>
                  <li>They have a rapid onset of contractions.</li>
                  <li>They are resistant to fatigue.</li>
                  <li>They primarily use anaerobic metabolism.</li>
                  <li>They can exhibit tetanus.</li>
                </ul>
                <p><strong>Correct Answer:</strong> They are resistant to fatigue.</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>The correct order for the smallest to the largest unit of organization in muscle tissue is ________.</strong></p>
                <ul>
                  <li>myofibril, muscle fiber, filament, fascicle</li>
                  <li>filament, myofibril, muscle fiber, fascicle</li>
                  <li>fascicle, filament, muscle fiber, myofibril</li>
                  <li>muscle fiber, fascicle, filament, myofibril</li>
                </ul>
                <p><strong>Correct Answer:</strong> filament, myofibril, muscle fiber, fascicle</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>Depolarization of the sarcolemma means ________.</strong></p>
                <ul>
                  <li>the inside of the membrane has become more negative as sodium ions accumulate</li>
                  <li>the sarcolemma has completely lost any electrical charge</li>
                  <li>the inside of the membrane has become less negative as sodium ions accumulate</li>
                  <li>the outside of the membrane has become less negative as sodium ions accumulate</li>
                </ul>
                <p><strong>Correct Answer:</strong> the inside of the membrane has become less negative as sodium ions accumulate</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 6</h3>
                <p><strong>Which cell type helps to repair injured muscle fibers?</strong></p>
                <ul>
                  <li>myoblast cells</li>
                  <li>ganglion cells</li>
                  <li>satellite cells</li>
                  <li>myotube cells</li>
                </ul>
                <p><strong>Correct Answer:</strong> satellite cells</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 7</h3>
                <p><strong>In relaxed muscle, the myosin-binding site on actin is blocked by ________.</strong></p>
                <ul>
                  <li>tropomyosin</li>
                  <li>myoglobin</li>
                  <li>titin</li>
                  <li>troponin</li>
                </ul>
                <p><strong>Correct Answer:</strong> tropomyosin</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 8</h3>
                <p><strong>Muscle relaxation occurs when ________.</strong></p>
                <ul>
                  <li>calcium ions are actively transported into the sarcoplasmic reticulum</li>
                  <li>calcium ions diffuse out of the sarcoplasmic reticulum</li>
                  <li>calcium ions diffuse into the sarcoplasmic reticulum</li>
                  <li>calcium ions are actively transported out of the sarcoplasmic reticulum</li>
                </ul>
                <p><strong>Correct Answer:</strong> calcium ions are actively transported into the sarcoplasmic reticulum</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 9</h3>
                <p><strong>Thin and thick filaments are organized into functional units called ________.</strong></p>
                <ul>
                  <li>myofilaments</li>
                  <li>sarcomeres</li>
                  <li>myofibrils</li>
                  <li>T-tubules</li>
                </ul>
                <p><strong>Correct Answer:</strong> sarcomeres</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 10</h3>
                <p><strong>This term describes the cell structure that anchors the ends of cardiac muscle fibers to allow contraction to occur.</strong></p>
                <ul>
                  <li>epimysium</li>
                  <li>desmosome</li>
                  <li>endomysium</li>
                  <li>calmodulin</li>
                </ul>
                <p><strong>Correct Answer:</strong> desmosome</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 11</h3>
                <p><strong>During which phase of a twitch in a muscle fiber is tension the greatest?</strong></p>
                <ul>
                  <li>relaxation phase</li>
                  <li>repolarization phase</li>
                  <li>contraction phase</li>
                  <li>resting phase</li>
                </ul>
                <p><strong>Correct Answer:</strong> contraction phase</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 12</h3>
                <p><strong>Muscle fatigue is caused by ________.</strong></p>
                <ul>
                  <li>buildup of ATP and pyruvic acid levels</li>
                  <li>buildup of ATP and lactic acid levels</li>
                  <li>exhaustion of energy reserves and buildup of lactic acid levels</li>
                  <li>exhaustion of energy reserves and buildup of pyruvic acid levels</li>
                </ul>
                <p><strong>Correct Answer:</strong> exhaustion of energy reserves and buildup of lactic acid levels</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 13</h3>
                <p><strong>A sprinter would experience muscle fatigue sooner than a marathon runner due to ________.</strong></p>
                <ul>
                  <li>anaerobic metabolism in the muscles of the marathon runner</li>
                  <li>glycolysis in the muscles of the marathon runner</li>
                  <li>aerobic metabolism in the muscles of the sprinter</li>
                  <li>anaerobic metabolism in the muscles of the sprinter</li>
                </ul>
                <p><strong>Correct Answer:</strong> anaerobic metabolism in the muscles of the sprinter</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 14</h3>
                <p><strong>What aspect of creatine phosphate allows it to supply energy to muscles?</strong></p>
                <ul>
                  <li>ATPase activity</li>
                  <li>phosphate bonds</li>
                  <li>carbon bonds</li>
                  <li>hydrogen bonds</li>
                </ul>
                <p><strong>Correct Answer:</strong> phosphate bonds</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 15</h3>
                <p><strong>Cardiac muscles differ from skeletal muscles in that they ________.</strong></p>
                <ul>
                  <li>contain myofibrils</li>
                  <li>are striated</li>
                  <li>contain intercalated discs</li>
                  <li>utilize aerobic metabolism</li>
                </ul>
                <p><strong>Correct Answer:</strong> contain intercalated discs</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 16</h3>
                <p><strong>If cardiac muscle cells were prevented from undergoing aerobic metabolism, they ultimately would ________.</strong></p>
                <ul>
                  <li>synthesize ATP</li>
                  <li>stop contracting</li>
                  <li>start contracting</li>
                  <li>undergo glycolysis</li>
                </ul>
                <p><strong>Correct Answer:</strong> stop contracting</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 17</h3>
                <p><strong>Smooth muscles differ from skeletal and cardiac muscles in that they ________.</strong></p>
                <ul>
                  <li>lack myosin</li>
                  <li>lack myofibrils</li>
                  <li>are under voluntary control</li>
                  <li>lack actin</li>
                </ul>
                <p><strong>Correct Answer:</strong> lack myofibrils</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 18</h3>
                <p><strong>Which of the following statements describes fast muscle cells?</strong></p>
                <ul>
                  <li>They cannot exhibit tetanus.</li>
                  <li>They primarily use amino acids.</li>
                  <li>They have a slow onset of contractions.</li>
                  <li>They can produce a lot of force and power for a short time.</li>
                </ul>
                <p><strong>Correct Answer:</strong> They can produce a lot of force and power for a short time.</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 19</h3>
                <p><strong>If cardiac muscle cells were prevented from undergoing aerobic metabolism, they ultimately would ________.</strong></p>
                <ul>
                  <li>stop contracting</li>
                  <li>start contracting</li>
                  <li>undergo glycolysis</li>
                  <li>synthesize ATP</li>
                </ul>
                <p><strong>Correct Answer:</strong> stop contracting</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 20</h3>
                <p><strong>Abnormally low muscle tone caused by the absence of low-level contractions is known as _________________. </strong></p>
                <ul>
                  <li>hyperplasia</li>
                  <li>hypertonia</li>
                  <li>hypertrophy</li>
                  <li>hypotonia</li>
                </ul>
                <p><strong>Correct Answer:</strong> hypotonia</p>
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
                <p><strong>An action potential releases stores of water.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>T-tubules crisscross the cells.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>Depolarization always causes an action potential.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>The sacroplasmic reticulum is the main storage space for Calcium in muscle cells.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>Troponin binds to calcium thus moving tropomyosin off the myosin binding sites.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 11 - Quiz</h3>
			<article>
                <h3>Question 1</h3>
                <p><strong>Which of the following is unique to the muscles of facial expression?</strong></p>
                <ul>
                  <li>They only insert onto the facial bones.</li>
                  <li>They insert onto the cartilage found around the face.</li>
                  <li>They all originate from the scalp musculature.</li>
                  <li>They insert into the skin.</li>
                </ul>
                <p><strong>Correct Answer:</strong> They insert into the skin.</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Which of the following helps an agonist work?</strong></p>
                <ul>
                  <li>a synergist</li>
                  <li>a fixator</li>
                  <li>an antagonist</li>
                  <li>an insertion</li>
                </ul>
                <p><strong>Correct Answer:</strong> a synergist</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>Which muscle produces movement that allows you to cross your legs?</strong></p>
                <ul>
                  <li>the piriformis</li>
                  <li>the gluteus maximus</li>
                  <li>the sartorius</li>
                  <li>the gracilis</li>
                </ul>
                <p><strong>Correct Answer:</strong> the sartorius</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>Which is moved the least during muscle contraction?</strong></p>
                <ul>
                  <li>the ligaments</li>
                  <li>the joints</li>
                  <li>the insertion</li>
                  <li>the origin</li>
                </ul>
                <p><strong>Correct Answer:</strong> the origin</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>Which muscle has a convergent pattern of fascicles?</strong></p>
                <ul>
                  <li>rectus femoris</li>
                  <li>biceps brachii</li>
                  <li>pectoralis major</li>
                  <li>gluteus maximus</li>
                </ul>
                <p><strong>Correct Answer:</strong> pectoralis major</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 6</h3>
                <p><strong>The small muscle on the lateral posterior elbow that extends the forearm is the ________________.</strong></p>
                <ul>
                  <li>piriformis</li>
                  <li>anconeus</li>
                  <li>brachioradialis</li>
                  <li>brevis</li>
                </ul>
                <p><strong>Correct Answer:</strong> anconeus</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 7</h3>
                <p><strong>Which arrangement best describes a bipennate muscle?</strong></p>
                <ul>
                  <li>The muscle fibers feed in on an angle to a long tendon from all directions.</li>
                  <li>The muscle fibers feed in on an angle to a long tendon from one side.</li>
                  <li>The muscle fibers feed in on an angle to a long tendon from both sides.</li>
                  <li>The muscle fibers on one side of a tendon feed into it at a certain angle and muscle fibers on the other side of the tendon feed into it at the opposite angle.</li>
                </ul>
                <p><strong>Correct Answer:</strong> The muscle fibers feed in on an angle to a long tendon from both sides.</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 8</h3>
                <p><strong>The location of a muscle’s insertion and origin can determine ________.</strong></p>
                <ul>
                  <li>type of movement</li>
                  <li>action</li>
                  <li>all of these</li>
                  <li>muscle name</li>
                </ul>
                <p><strong>Correct Answer:</strong> all of these</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 9</h3>
                <p><strong>Which of the following abdominal muscles is not a part of the anterior abdominal wall?</strong></p>
                <ul>
                  <li>rectus abdominis</li>
                  <li>interior oblique</li>
                  <li>quadratus lumborum</li>
                  <li>exterior oblique</li>
                </ul>
                <p><strong>Correct Answer:</strong> quadratus lumborum</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 10</h3>
                <p><strong>Which of the following is a prime mover in head flexion?</strong></p>
                <ul>
                  <li>corrugator supercilii</li>
                  <li>sternocleidomastoid</li>
                  <li>masseter</li>
                  <li>occipitofrontalis</li>
                </ul>
                <p><strong>Correct Answer:</strong> sternocleidomastoid</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 11</h3>
                <p><strong>Where is the inferior oblique muscle located?</strong></p>
                <ul>
                  <li>in the eye socket</li>
                  <li>in the abdomen</li>
                  <li>in the face</li>
                  <li>in the anterior neck</li>
                </ul>
                <p><strong>Correct Answer:</strong> in the eye socket</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 12</h3>
                <p><strong>What is the action of the masseter?</strong></p>
                <ul>
                  <li>closing the eye</li>
                  <li>swallowing</li>
                  <li>moving the lips</li>
                  <li>chewing</li>
                </ul>
                <p><strong>Correct Answer:</strong> chewing</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 13</h3>
                <p><strong>What is the largest muscle in the lower leg?</strong></p>
                <ul>
                  <li>gastrocnemius</li>
                  <li>tibialis posterior</li>
                  <li>soleus</li>
                  <li>tibialis anterior</li>
                </ul>
                <p><strong>Correct Answer:</strong> gastrocnemius</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 14</h3>
                <p><strong>The names of the extrinsic tongue muscles commonly end in ________.</strong></p>
                <ul>
                  <li>glossus</li>
                  <li>hyoid</li>
                  <li>gluteus</li>
                  <li>glottis</li>
                </ul>
                <p><strong>Correct Answer:</strong> glossus</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 15</h3>
                <p><strong>Which muscle name does not make sense?</strong></p>
                <ul>
                  <li>extensor digitorum</li>
                  <li>gluteus minimus</li>
                  <li>biceps femoris</li>
                  <li>extensor minimus longus</li>
                </ul>
                <p><strong>Correct Answer:</strong> extensor minimus longus</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 16</h3>
                <p><strong>The pelvic girdle attaches the ________ to the axial skeleton.</strong></p>
                <ul>
                  <li>pelvis</li>
                  <li>arms</li>
                  <li>vertebrae</li>
                  <li>legs</li>
                </ul>
                <p><strong>Correct Answer:</strong> legs</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 17</h3>
                <p><strong>Which muscle pair plays a role in respiration?</strong></p>
                <ul>
                  <li>semispinalis cervicis, semispinalis thoracis</li>
                  <li>trapezius, rhomboids</li>
                  <li>diaphragm, scalene</li>
                  <li>intertransversarii, interspinales</li>
                </ul>
                <p><strong>Correct Answer:</strong> diaphragm, scalene</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 18</h3>
                <p><strong>Which muscle extends the forearm?</strong></p>
                <ul>
                  <li>brachialis</li>
                  <li>triceps brachii</li>
                  <li>biceps brachii</li>
                  <li>deltoid</li>
                </ul>
                <p><strong>Correct Answer:</strong> triceps brachii</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 19</h3>
                <p><strong>The vastus intermedius muscle is deep to which of the following muscles?</strong></p>
                <ul>
                  <li>rectus femoris</li>
                  <li>biceps femoris</li>
                  <li>vastus medialis</li>
                  <li>vastus lateralis</li>
                </ul>
                <p><strong>Correct Answer:</strong> rectus femoris</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 20</h3>
                <p><strong>The _______________________ muscle that makes up the levator ani along with the iliococcygeus.</strong></p>
                <ul>
                  <li>quadratus lumborum</li>
                  <li>posterior scalene</li>
                  <li>rectus abdominis</li>
                  <li>pubococcygeus</li>
                </ul>
                <p><strong>Correct Answer:</strong> pubococcygeus</p>
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
                <p><strong>The axon of a neuron is the head region of the neuron.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>There are a lot of sodium ions outside the axon.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>If a stimulus does not reach the Threshold, then an action potential will not occur.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>Sodium rushes into the cell once the threshold is reached.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>When Potassium leaves the cell, causing even more Sodium ions to flood the cell.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 12 - Quiz</h3>
			<article>
                <h3>Question 1</h3>
                <p><strong>Which of the following cavities contains a component of the central nervous system?</strong></p>
                <ul>
                  <li>cranial</li>
                  <li>pelvic</li>
                  <li>abdominal</li>
                  <li>thoracic</li>
                </ul>
                <p><strong>Correct Answer:</strong> cranial</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Which structure predominates in the white matter of the brain?</strong></p>
                <ul>
                  <li>myelinated axons</li>
                  <li>bundles of dendrites from the enteric nervous system</li>
                  <li>ganglia of the parasympathetic nerves</li>
                  <li>neuronal cell bodies</li>
                </ul>
                <p><strong>Correct Answer:</strong> myelinated axons</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>Which part of a neuron transmits an electrical signal to a target cell?</strong></p>
                <ul>
                  <li>soma</li>
                  <li>cell body</li>
                  <li>axon</li>
                  <li>dendrites</li>
                </ul>
                <p><strong>Correct Answer:</strong> axon</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>Which term describes a bundle of axons in the peripheral nervous system?</strong></p>
                <ul>
                  <li>tract</li>
                  <li>nucleus</li>
                  <li>ganglion</li>
                  <li>nerve</li>
                </ul>
                <p><strong>Correct Answer:</strong> nerve</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>Which functional division of the nervous system would be responsible for the physiological changes seen during exercise (e.g., increased heart rate and sweating)?</strong></p>
                <ul>
                  <li>somatic</li>
                  <li>central</li>
                  <li>enteric</li>
                  <li>autonomic</li>
                </ul>
                <p><strong>Correct Answer:</strong> autonomic</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 6</h3>
                <p><strong>Which part of a neuron contains the nucleus?</strong></p>
                <ul>
                  <li>synaptic end bulb</li>
                  <li>axon</li>
                  <li>soma</li>
                  <li>dendrite</li>
                </ul>
                <p><strong>Correct Answer:</strong> soma</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 7</h3>
                <p><strong>What type of receptor requires an effector protein to initiate a signal?</strong></p>
                <ul>
                  <li>biogenic amine</li>
                  <li>ionotropic receptor</li>
                  <li>cholinergic system</li>
                  <li>metabotropic receptor</li>
                </ul>
                <p><strong>Correct Answer:</strong> metabotropic receptor</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 8</h3>
                <p><strong>Voltage-gated Na+ channels open upon reaching what state?</strong></p>
                <ul>
                  <li>threshold</li>
                  <li>repolarization</li>
                  <li>resting potential</li>
                  <li>overshoot</li>
                </ul>
                <p><strong>Correct Answer:</strong> threshold</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 9</h3>
                <p><strong>Which of the following neurotransmitters is associated with inhibition exclusively?</strong></p>
                <ul>
                  <li>norepinephrine</li>
                  <li>glutamate</li>
                  <li>GABA</li>
                  <li>acetylcholine</li>
                </ul>
                <p><strong>Correct Answer:</strong> GABA</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 10</h3>
                <p><strong>What two types of macromolecules are the main components of myelin?</strong></p>
                <ul>
                  <li>lipids and proteins</li>
                  <li>proteins and nucleic acids</li>
                  <li>carbohydrates and nucleic acids</li>
                  <li>carbohydrates and lipids</li>
                </ul>
                <p><strong>Correct Answer:</strong> lipids and proteins</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 11</h3>
                <p><strong>The ______________ is a single process of the neuron that carries an electrical signal (action potential) away from the cell body toward a target cell.</strong></p>
                <ul>
                  <li>astrocyte</li>
                  <li>glial</li>
                  <li>axon</li>
                  <li>dendrite</li>
                </ul>
                <p><strong>Correct Answer:</strong> axon</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 12</h3>
                <p><strong>Which of these locations is where the greatest level of integration is taking place in the example of testing the temperature of the shower?</strong></p>
                <ul>
                  <li>thalamus</li>
                  <li>spinal cord</li>
                  <li>skeletal muscle</li>
                  <li>cerebral cortex</li>
                </ul>
                <p><strong>Correct Answer:</strong> cerebral cortex</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 13</h3>
                <p><strong>What neurotransmitter is released at the neuromuscular junction?</strong></p>
                <ul>
                  <li>serotonin</li>
                  <li>dopamine</li>
                  <li>acetylcholine</li>
                  <li>norepinephrine</li>
                </ul>
                <p><strong>Correct Answer:</strong> acetylcholine</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 14</h3>
                <p><strong>How long does all the signaling through the sensory pathway, within the central nervous system, and through the motor command pathway take?</strong></p>
                <ul>
                  <li>1 to 2 seconds</li>
                  <li>varies with graded potential</li>
                  <li>1 to 2 minutes</li>
                  <li>fraction of a second</li>
                </ul>
                <p><strong>Correct Answer:</strong> fraction of a second</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 15</h3>
                <p><strong>What type of glial cell provides myelin for the axons in a tract?</strong></p>
                <ul>
                  <li>astrocyte</li>
                  <li>satellite cell</li>
                  <li>oligodendrocyte</li>
                  <li>Schwann cell</li>
                </ul>
                <p><strong>Correct Answer:</strong> oligodendrocyte</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 16</h3>
                <p><strong>What ion enters a neuron causing depolarization of the cell membrane?</strong></p>
                <ul>
                  <li>chloride</li>
                  <li>sodium</li>
                  <li>potassium</li>
                  <li>phosphate</li>
                </ul>
                <p><strong>Correct Answer:</strong> sodium</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 17</h3>
                <p><strong>What does a mechanically gated channel respond to?</strong></p>
                <ul>
                  <li>physical stimulus</li>
                  <li>increase in resistance</li>
                  <li>chemical stimulus</li>
                  <li>decrease in resistance</li>
                </ul>
                <p><strong>Correct Answer:</strong> physical stimulus</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 18</h3>
                <p><strong>Which of the following voltages would most likely be measured during the relative refractory period?</strong></p>
                <ul>
                  <li>0 mV</li>
                  <li>-45 mV</li>
                  <li>-80 mv</li>
                  <li>+30 mV</li>
                </ul>
                <p><strong>Correct Answer:</strong> -80 mv</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 19</h3>
                <p><strong>What neurotransmitter is released at the neuromuscular junction?</strong></p>
                <ul>
                  <li>acetylcholine</li>
                  <li>dopamine</li>
                  <li>norepinephrine</li>
                  <li>serotonin</li>
                </ul>
                <p><strong>Correct Answer:</strong> acetylcholine</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 20</h3>
                <p><strong>The ion channel that opens when a physical event directly affects the structure of the protein is called:</strong></p>
                <ul>
                  <li>mechanically gated channel</li>
                  <li>ligand-gated channels</li>
                  <li>leakage channel</li>
                  <li>ionotropic channel</li>
                </ul>
                <p><strong>Correct Answer:</strong> mechanically gated channel</p>
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
                <p><strong>The plasma membrane is hydrophilic.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Adenylyl cyclase is a membrane enzyme.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>cAMP forms outside the cell.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>Melatonin is produced in the Pineal Gland.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>Melatonin does not produce an antioxidant effect.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 17 - Quiz</h3>
			<article>
                <h3>Question 1</h3>
                <p><strong>Endocrine glands ________.</strong></p>
                <ul>
                  <li>include sebaceous glands and sweat glands</li>
                  <li>secrete chemical messengers that travel in the bloodstream</li>
                  <li>release neurotransmitters into the synaptic cleft</li>
                  <li>secrete hormones that travel through a duct to the target organs</li>
                </ul>
                <p><strong>Correct Answer:</strong> secrete chemical messengers that travel in the bloodstream</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Iodide ions cross from the bloodstream into follicle cells via ________.</strong></p>
                <ul>
                  <li>simple diffusion</li>
                  <li>facilitated diffusion</li>
                  <li>osmosis</li>
                  <li>active transport</li>
                </ul>
                <p><strong>Correct Answer:</strong> active transport</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>A newly developed pesticide has been observed to bind to an intracellular hormone receptor. If ingested, residue from this pesticide could disrupt levels of ________.</strong></p>
                <ul>
                  <li>insulin</li>
                  <li>melatonin</li>
                  <li>growth hormone</li>
                  <li>thyroid hormone</li>
                </ul>
                <p><strong>Correct Answer:</strong> thyroid hormone</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>Chemical signaling that affects neighboring cells is called ________.</strong></p>
                <ul>
                  <li>autocrine</li>
                  <li>paracrine</li>
                  <li>endocrine</li>
                  <li>neuron</li>
                </ul>
                <p><strong>Correct Answer:</strong> paracrine</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>Athletes may take synthetic EPO to boost their ________.</strong></p>
                <ul>
                  <li>muscle mass</li>
                  <li>blood calcium levels</li>
                  <li>blood oxygen levels</li>
                  <li>secretion of growth hormone</li>
                </ul>
                <p><strong>Correct Answer:</strong> blood oxygen levels</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 6</h3>
                <p><strong>Which of the following is an anterior pituitary hormone?</strong></p>
                <ul>
                  <li>cortisol</li>
                  <li>ADH</li>
                  <li>TSH</li>
                  <li>oxytocin</li>
                </ul>
                <p><strong>Correct Answer:</strong> TSH</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 7</h3>
                <p><strong>The adrenal glands are attached superiorly to which organ?</strong></p>
                <ul>
                  <li>hypothalamus</li>
                  <li>thyroid</li>
                  <li>kidneys</li>
                  <li>liver</li>
                </ul>
                <p><strong>Correct Answer:</strong> kidneys</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 8</h3>
                <p><strong>In the elderly, decreased thyroid function causes ________.</strong></p>
                <ul>
                  <li>decreased body fat</li>
                  <li>decreased basal metabolic rate</li>
                  <li>increased tolerance for cold</li>
                  <li>osteoporosis</li>
                </ul>
                <p><strong>Correct Answer:</strong> decreased basal metabolic rate</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 9</h3>
                <p><strong>This is a disorder in adults caused when abnormally high levels of GH trigger growth of bones in the face, hands, and feet.</strong></p>
                <ul>
                  <li>aldosterone</li>
                  <li>gigantism</li>
                  <li>acromegaly</li>
                  <li>hyperglycemia</li>
                </ul>
                <p><strong>Correct Answer:</strong> acromegaly</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 10</h3>
                <p><strong>The anterior pituitary gland develops from which embryonic germ layer?</strong></p>
                <ul>
                  <li>oral ectoderm</li>
                  <li>mesoderm</li>
                  <li>neural ectoderm</li>
                  <li>endoderm</li>
                </ul>
                <p><strong>Correct Answer:</strong> oral ectoderm</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 11</h3>
                <p><strong>Which of the following hormones contributes to the regulation of the body’s fluid and electrolyte balance?</strong></p>
                <ul>
                  <li>all of the above</li>
                  <li>luteinizing hormone</li>
                  <li>adrenocorticotropic hormone</li>
                  <li>antidiuretic hormone</li>
                </ul>
                <p><strong>Correct Answer:</strong> antidiuretic hormone</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 12</h3>
                <p><strong>Which of the following statements about the thyroid gland is true?</strong></p>
                <ul>
                  <li>The parathyroid glands are embedded within it.</li>
                  <li>all of the above</li>
                  <li>It manufactures three hormones.</li>
                  <li>It is located anterior to the trachea and inferior to the larynx.</li>
                </ul>
                <p><strong>Correct Answer:</strong> all of the above</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 13</h3>
                <p><strong>The secretion of thyroid hormones is controlled by _______ .</strong></p>
                <ul>
                  <li>thyroglobulin from the thyroid’s parafollicular cells</li>
                  <li>thyroxine from the anterior pituitary</li>
                  <li>TSH from the hypothalamus</li>
                  <li>TSH from the anterior pituitary</li>
                </ul>
                <p><strong>Correct Answer:</strong> TSH from the anterior pituitary</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 14</h3>
                <p><strong>The hypothalamus is functionally and anatomically connected to the posterior pituitary lobe by a bridge of ________.</strong></p>
                <ul>
                  <li>bone</li>
                  <li>nerve axons</li>
                  <li>blood vessels</li>
                  <li>cartilage</li>
                </ul>
                <p><strong>Correct Answer:</strong> nerve axons</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 15</h3>
                <p><strong>The development of a goiter indicates that ________.</strong></p>
                <ul>
                  <li>there is hypertrophy of the thyroid’s follicle cells</li>
                  <li>the anterior pituitary is abnormally enlarged</li>
                  <li>there is an excessive accumulation of colloid in the thyroid follicles</li>
                  <li>the anterior pituitary is secreting excessive growth hormone</li>
                </ul>
                <p><strong>Correct Answer:</strong> there is an excessive accumulation of colloid in the thyroid follicles</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 16</h3>
                <p><strong>When blood calcium levels are low, PTH stimulates _______ .</strong></p>
                <ul>
                  <li>the activity of osteoblasts</li>
                  <li>the activity of osteoclasts</li>
                  <li>a reduction in calcium absorption from the intestines</li>
                  <li>urinary excretion of calcium by the kidneys</li>
                </ul>
                <p><strong>Correct Answer:</strong> the activity of osteoclasts</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 17</h3>
                <p><strong>Which of the following can result from hyperparathyroidism?</strong></p>
                <ul>
                  <li>all of the above</li>
                  <li>fractures</li>
                  <li>convulsions</li>
                  <li>increased bone deposition</li>
                </ul>
                <p><strong>Correct Answer:</strong> fractures</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 18</h3>
                <p><strong>What cells secrete melatonin?</strong></p>
                <ul>
                  <li>retinal cells</li>
                  <li>suprachiasmatic nucleus cells</li>
                  <li>melanocytes</li>
                  <li>pinealocytes</li>
                </ul>
                <p><strong>Correct Answer:</strong> pinealocytes</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 19</h3>
                <p><strong>The gonads produce what class of hormones?</strong></p>
                <ul>
                  <li>amine hormones</li>
                  <li>catecholamines</li>
                  <li>peptide hormones</li>
                  <li>steroid hormones</li>
                </ul>
                <p><strong>Correct Answer:</strong> steroid hormones</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 20</h3>
                <p><strong>Which region of the diencephalon is inferior to the thalamus that functions in neural and endocrine signaling?</strong></p>
                <ul>
                  <li>posterior pituitary gland</li>
                  <li>infundibulum</li>
                  <li>anterior pituitary gland</li>
                  <li>hypothalamus</li>
                </ul>
                <p><strong>Correct Answer:</strong> hypothalamus</p>
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
                <p><strong>Until the 21st century, no one was really able to see a heart pump blood.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>The human heart is a 2-chambered organ.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>In reality, mammals have a figure 8 circulation in terms of blood movement.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>The heart pumps about 2 billion beats in a lifetime.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>The atria sit below the ventricles in a mammalian heart.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 19 - Quiz</h3>
			<article>
                <h3>Question 1</h3>
                <p><strong>Which primitive area of the heart will give rise to the right ventricle?</strong></p>
                <ul>
                  <li>primitive ventricle</li>
                  <li>truncus arteriosus</li>
                  <li>bulbus cordis</li>
                  <li>sinus venosus</li>
                </ul>
                <p><strong>Correct Answer:</strong> bulbus cordis</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Which of the following lists the valves in the order through which the blood flows from the vena cava through the heart?</strong></p>
                <ul>
                  <li>mitral, pulmonary semilunar, bicuspid, aortic semilunar</li>
                  <li>bicuspid, aortic semilunar, tricuspid, pulmonary semilunar</li>
                  <li>aortic semilunar, pulmonary semilunar, tricuspid, bicuspid</li>
                  <li>tricuspid, pulmonary semilunar, bicuspid, aortic semilunar</li>
                </ul>
                <p><strong>Correct Answer:</strong> tricuspid, pulmonary semilunar, bicuspid, aortic semilunar</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>The pulmonary trunk and aorta are derived from which primitive heart structure?</strong></p>
                <ul>
                  <li>bulbus cordis</li>
                  <li>sinus venosus</li>
                  <li>truncus arteriosus</li>
                  <li>primitive ventricle</li>
                </ul>
                <p><strong>Correct Answer:</strong> truncus arteriosus</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>The ________ layer secretes chemicals that help to regulate ionic environments and strength of contraction and serve as powerful vasoconstrictors.</strong></p>
                <ul>
                  <li>endocardium</li>
                  <li>myocardium</li>
                  <li>pericardial sac</li>
                  <li>epicardium</li>
                </ul>
                <p><strong>Correct Answer:</strong> endocardium</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>The myocardium would be the thickest in the ________.</strong></p>
                <ul>
                  <li>right atrium</li>
                  <li>right ventricle</li>
                  <li>left ventricle</li>
                  <li>left atrium</li>
                </ul>
                <p><strong>Correct Answer:</strong> left ventricle</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 6</h3>
                <p><strong>In which septum is it normal to find openings in the adult?</strong></p>
                <ul>
                  <li>interventricular septum</li>
                  <li>interatrial septum</li>
                  <li>atrioventricular septum</li>
                  <li>all of the above</li>
                </ul>
                <p><strong>Correct Answer:</strong> atrioventricular septum</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 7</h3>
                <p><strong>Which of the following is unique to cardiac muscle cells?</strong></p>
                <ul>
                  <li>Only cardiac muscle contains a sarcoplasmic reticulum.</li>
                  <li>Only cardiac muscle is capable of autorhythmicity</li>
                  <li>Only cardiac muscle has a high concentration of mitochondria.</li>
                  <li>Only cardiac muscle has gap junctions.</li>
                </ul>
                <p><strong>Correct Answer:</strong> Only cardiac muscle is capable of autorhythmicity</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 8</h3>
                <p><strong>The _________________________ is the extension of an atrium visible on the superior surface of the heart.</strong></p>
                <ul>
                  <li>auricle</li>
                  <li>ventricle</li>
                  <li>aorta</li>
                  <li>pulmonary valve</li>
                </ul>
                <p><strong>Correct Answer:</strong> auricle</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 9</h3>
                <p><strong>The influx of which ion accounts for the plateau phase?</strong></p>
                <ul>
                  <li>chloride</li>
                  <li>potassium</li>
                  <li>sodium</li>
                  <li>calcium</li>
                </ul>
                <p><strong>Correct Answer:</strong> calcium</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 10</h3>
                <p><strong>Of the three germ layers that give rise to all adult tissues and organs, which gives rise to the heart?</strong></p>
                <ul>
                  <li>mesoderm</li>
                  <li>ectoderm</li>
                  <li>endoderm</li>
                  <li>placenta</li>
                </ul>
                <p><strong>Correct Answer:</strong> mesoderm</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 11</h3>
                <p><strong>Which component of the heart conduction system would have the slowest rate of firing?</strong></p>
                <ul>
                  <li>atrioventricular node</li>
                  <li>bundle branches</li>
                  <li>atrioventricular bundle</li>
                  <li>Purkinje fibers</li>
                </ul>
                <p><strong>Correct Answer:</strong> atrioventricular node</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 12</h3>
                <p><strong>Which of the following is not important in preventing backflow of blood?</strong></p>
                <ul>
                  <li>AV valves</li>
                  <li>papillary muscles</li>
                  <li>chordae tendineae</li>
                  <li>endocardium</li>
                </ul>
                <p><strong>Correct Answer:</strong> endocardium</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 13</h3>
                <p><strong>Most blood enters the ventricle during ________.</strong></p>
                <ul>
                  <li>atrial diastole</li>
                  <li>ventricular systole</li>
                  <li>isovolumic contraction</li>
                  <li>atrial systole</li>
                </ul>
                <p><strong>Correct Answer:</strong> atrial diastole</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 14</h3>
                <p><strong>The first heart sound represents which portion of the cardiac cycle?</strong></p>
                <ul>
                  <li>closing of the atrioventricular valves</li>
                  <li>closing of the semilunar valves</li>
                  <li>atrial systole</li>
                  <li>ventricular systole</li>
                </ul>
                <p><strong>Correct Answer:</strong> closing of the atrioventricular valves</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 15</h3>
                <p><strong>The force the heart must overcome to pump blood is known as ________.</strong></p>
                <ul>
                  <li>cardiac output</li>
                  <li>stroke volume</li>
                  <li>afterload</li>
                  <li>preload</li>
                </ul>
                <p><strong>Correct Answer:</strong> afterload</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 16</h3>
                <p><strong>The earliest organ to form and begin function within the developing human is the ________.</strong></p>
                <ul>
                  <li>lungs</li>
                  <li>stomach</li>
                  <li>heart</li>
                  <li>brain</li>
                </ul>
                <p><strong>Correct Answer:</strong> heart</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 17</h3>
                <p><strong>Of the three germ layers that give rise to all adult tissues and organs, which gives rise to the heart?</strong></p>
                <ul>
                  <li>ectoderm</li>
                  <li>mesoderm</li>
                  <li>endoderm</li>
                  <li>placenta</li>
                </ul>
                <p><strong>Correct Answer:</strong> mesoderm</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 18</h3>
                <p><strong>The cardiovascular centers are located in which area of the brain?</strong></p>
                <ul>
                  <li>microglia</li>
                  <li>medulla oblongata</li>
                  <li>mesencephalon (midbrain)</li>
                  <li>pons</li>
                </ul>
                <p><strong>Correct Answer:</strong> medulla oblongata</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 19</h3>
                <p><strong>The two tubes that eventually fuse to form the heart are referred to as the ________.</strong></p>
                <ul>
                  <li>endocardial tubes</li>
                  <li>cardiogenic region</li>
                  <li>primitive heart tubes</li>
                  <li>cardiogenic tubes</li>
                </ul>
                <p><strong>Correct Answer:</strong> endocardial tubes</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 20</h3>
                <p><strong>Which of the following is the innermost layer of the serous pericardium and the outermost layer of the heart wall?</strong></p>
                <ul>
                  <li>mesocardium</li>
                  <li>endocardium</li>
                  <li>epicardium</li>
                  <li>ectocardium</li>
                </ul>
                <p><strong>Correct Answer:</strong> epicardium</p>
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
                <p><strong>Capillaries are responsible for gas exchange.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Capillaries are not thin.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>Interstitial fluid contains water and dissolved nutrients.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>There are many many capillaries throughout your body, nearly 50,000 miles if they were to be streched out.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>As the blood continues to move throughout the capillaries, it gains speed.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 21 - Quiz</h3>
			<article>
                <h3>Question 1</h3>
                <p><strong>Which structure allows lymph from the lower right limb to enter the bloodstream?</strong></p>
                <ul>
                  <li>right lymphatic trunk</li>
                  <li>thoracic duct</li>
                  <li>right lymphatic duct</li>
                  <li>left lymphatic trunk</li>
                </ul>
                <p><strong>Correct Answer:</strong> thoracic duct</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>The ductus venosus is a shunt that allows ___________________________________.</strong></p>
                <ul>
                  <li>most freshly oxygenated blood to flow into the fetal heart</li>
                  <li>fetal blood to flow from the right ventricle to the left ventricle</li>
                  <li>most oxygen-depleted fetal blood to flow directly into the fetal pulmonary trunk</li>
                  <li>fetal blood to flow from the right atrium to the left atrium</li>
                </ul>
                <p><strong>Correct Answer:</strong> most freshly oxygenated blood to flow into the fetal heart</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>The development of new blood vessels from existing vessels is called _____________________.</strong></p>
                <ul>
                  <li>periogenesis</li>
                  <li>ectogenesis</li>
                  <li>epigenesis</li>
                  <li>angiogenesis</li>
                </ul>
                <p><strong>Correct Answer:</strong> angiogenesis</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>Which of the following cells would be most active in early, antiviral immune responses the first time one is exposed to pathogen?</strong></p>
                <ul>
                  <li>natural killer cell</li>
                  <li>macrophage</li>
                  <li>T cell</li>
                  <li>neutrophil</li>
                </ul>
                <p><strong>Correct Answer:</strong> natural killer cell</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>Which of the following statements is true?</strong></p>
                <ul>
                  <li>All of the above are true.</li>
                  <li>Two umbilical veins carry oxygen-depleted blood from the fetal circulation to the placenta.</li>
                  <li>Two umbilical arteries carry oxygen-depleted blood to the fetal lungs.</li>
                  <li>One umbilical vein carries oxygen-rich blood from the placenta to the fetal heart.</li>
                </ul>
                <p><strong>Correct Answer:</strong> One umbilical vein carries oxygen-rich blood from the placenta to the fetal heart.</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 6</h3>
                <p><strong>Removing functionality from a B cell without killing it is called ________.</strong></p>
                <ul>
                  <li>clonal anergy</li>
                  <li>clonal expansion</li>
                  <li>clonal selection</li>
                  <li>clonal deletion</li>
                </ul>
                <p><strong>Correct Answer:</strong> clonal anergy</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 7</h3>
                <p><strong>Which of the following cells is phagocytic?</strong></p>
                <ul>
                  <li>macrophage</li>
                  <li>B cell</li>
                  <li>plasma cell</li>
                  <li>NK cell</li>
                </ul>
                <p><strong>Correct Answer:</strong> macrophage</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 8</h3>
                <p><strong>Which of the following signs is not characteristic of inflammation?</strong></p>
                <ul>
                  <li>redness</li>
                  <li>swelling</li>
                  <li>pain</li>
                  <li>cold</li>
                </ul>
                <p><strong>Correct Answer:</strong> cold</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 9</h3>
                <p><strong>Enhanced phagocytosis of a cell by the binding of a specific protein is called ________.</strong></p>
                <ul>
                  <li>complement activation</li>
                  <li>endocytosis</li>
                  <li>opsonization</li>
                  <li>anaphylaxis</li>
                </ul>
                <p><strong>Correct Answer:</strong> opsonization</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 10</h3>
                <p><strong>Which of the following leads to the redness of inflammation?</strong></p>
                <ul>
                  <li>anaphylactic shock</li>
                  <li>complement activation</li>
                  <li>increased vascular permeability</li>
                  <li>increased blood flow</li>
                </ul>
                <p><strong>Correct Answer:</strong> increased blood flow</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 11</h3>
                <p><strong>T cells that secrete cytokines that help antibody responses are called ________.</strong></p>
                <ul>
                  <li>thymocytes</li>
                  <li>Th1</li>
                  <li>regulatory T cells</li>
                  <li>Th2</li>
                </ul>
                <p><strong>Correct Answer:</strong> Th2</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 12</h3>
                <p><strong>The taking in of antigen and digesting it for later presentation is called ________.</strong></p>
                <ul>
                  <li>antigen presentation</li>
                  <li>endocytosis</li>
                  <li>exocytosis</li>
                  <li>antigen processing</li>
                </ul>
                <p><strong>Correct Answer:</strong> antigen processing</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 13</h3>
                <p><strong>Blood islands are ____________________________________.</strong></p>
                <ul>
                  <li>clusters of blood-filtering cells in the placenta</li>
                  <li>masses of developing blood vessels and formed elements scattered throughout the embryonic disc</li>
                  <li>masses of pluripotent stem cells scattered throughout the fetal bone marrow</li>
                  <li>vascular tubes that give rise to the embryonic tubular heart</li>
                </ul>
                <p><strong>Correct Answer:</strong> masses of developing blood vessels and formed elements scattered throughout the embryonic disc</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 14</h3>
                <p><strong>Why is clonal expansion so important?</strong></p>
                <ul>
                  <li>to kill target cells</li>
                  <li>to secrete cytokines</li>
                  <li>to select for specific cells</li>
                  <li>to increase the numbers of specific cells</li>
                </ul>
                <p><strong>Correct Answer:</strong> to increase the numbers of specific cells</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 15</h3>
                <p><strong>Which of the lymphoid nodules is most likely to see food antigens first?</strong></p>
                <ul>
                  <li>bronchus-associated lymphoid tissue</li>
                  <li>mucosa-associated lymphoid tissue</li>
                  <li>Peyer’s patches</li>
                  <li>tonsils</li>
                </ul>
                <p><strong>Correct Answer:</strong> tonsils</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 16</h3>
                <p><strong>The elimination of self-reactive thymocytes is called ________.</strong></p>
                <ul>
                  <li>positive selection.</li>
                  <li>clonal selection.</li>
                  <li>negative selection.</li>
                  <li>tolerance</li>
                </ul>
                <p><strong>Correct Answer:</strong> negative selection.</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 17</h3>
                <p><strong>Which type of T cell is most effective against viruses?</strong></p>
                <ul>
                  <li>Th1</li>
                  <li>TH2</li>
                  <li>cytotoxic T cells</li>
                  <li>regulatory T cells</li>
                </ul>
                <p><strong>Correct Answer:</strong> cytotoxic T cells</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 18</h3>
                <p><strong>Which class of antibody crosses the placenta in pregnant women?</strong></p>
                <ul>
                  <li>IgA</li>
                  <li>IgB</li>
                  <li>IgE</li>
                  <li>IgG</li>
                </ul>
                <p><strong>Correct Answer:</strong> IgG</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 19</h3>
                <p><strong>Which enzymes in macrophages are important for clearing intracellular bacteria?</strong></p>
                <ul>
                  <li>mitochondrial</li>
                  <li>nuclear</li>
                  <li>metabolic</li>
                  <li>lysosomal</li>
                </ul>
                <p><strong>Correct Answer:</strong> lysosomal</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 20</h3>
                <p><strong>Which of the following arteries is a continuation of the external iliac artery after it passes through the body cavity?</strong></p>
                <ul>
                  <li>fibular</li>
                  <li>pulmonary</li>
                  <li>renal</li>
                  <li>femoral</li>
                </ul>
                <p><strong>Correct Answer:</strong> femoral</p>
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
                <p><strong>Oxygen is a molecule made from three oxygen atoms.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Oxygen is transported through blood.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>Alveoli are also known as capillaries.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>Hemoglobin is a special oxygen binding protein.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>When the partial pressure of oxygen becomes greater in the capillaries than the partial pressure of oxygen in the surrounding tissues, oxygen begins to move out of the capillaries into the surrounding tissue.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 22 - Quiz</h3>
			<article>
                <h3>Question 1</h3>
                <p><strong>A full complement of mature alveoli are present by ________.</strong></p>
                <ul>
                  <li>birth</li>
                  <li>early childhood, around 8 years of age</li>
                  <li>37 weeks</li>
                  <li>16 weeks</li>
                </ul>
                <p><strong>Correct Answer:</strong> early childhood, around 8 years of age</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Which of the following are structural features of the trachea?</strong></p>
                <ul>
                  <li>C-shaped cartilage</li>
                  <li>all of these</li>
                  <li>smooth muscle fibers</li>
                  <li>cilia</li>
                </ul>
                <p><strong>Correct Answer:</strong> all of these</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>A section of the lung that receives its own tertiary bronchus is called the ________.</strong></p>
                <ul>
                  <li>respiratory segment</li>
                  <li>bronchopulmonary segment</li>
                  <li>pulmonary lobule</li>
                  <li>interpulmonary segment</li>
                </ul>
                <p><strong>Correct Answer:</strong> bronchopulmonary segment</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>The ______________________ is a(n) opening that allows airflow between neighboring alveoli:</strong></p>
                <ul>
                  <li>alveolar duct</li>
                  <li>alveolar macrophage</li>
                  <li>alveolar sac</li>
                  <li>alveolar pore</li>
                </ul>
                <p><strong>Correct Answer:</strong> alveolar pore</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>The _________________ system consists of organs and structures that allow us to breathe by taking in oxygen and expelling carbon dioxide.</strong></p>
                <ul>
                  <li>bronchial</li>
                  <li>respiratory</li>
                  <li>interlobular</li>
                  <li>pulmonary</li>
                </ul>
                <p><strong>Correct Answer:</strong> respiratory</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 6</h3>
                <p><strong>When do fetal breathing movements begin?</strong></p>
                <ul>
                  <li>approximately week 37</li>
                  <li>about week 16</li>
                  <li>after birth</li>
                  <li>approximately week 20</li>
                </ul>
                <p><strong>Correct Answer:</strong> approximately week 20</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 7</h3>
                <p><strong>What is the function of the conchae in the nasal cavity?</strong></p>
                <ul>
                  <li>maintain surface tension</li>
                  <li>increase surface area</li>
                  <li>exchange gases</li>
                  <li>maintain air pressure</li>
                </ul>
                <p><strong>Correct Answer:</strong> increase surface area</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 8</h3>
                <p><strong>Gas flow decreases as ________ increases.</strong></p>
                <ul>
                  <li>airway diameter</li>
                  <li>friction</li>
                  <li>pressure</li>
                  <li>resistance</li>
                </ul>
                <p><strong>Correct Answer:</strong> resistance</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 9</h3>
                <p><strong>What happens to the fluid that remains in the lungs after birth?</strong></p>
                <ul>
                  <li>It lubricates the pleurae.</li>
                  <li>It is expelled shortly after birth.</li>
                  <li>It is absorbed shortly after birth.</li>
                  <li>It reduces the surface tension of the alveoli.</li>
                </ul>
                <p><strong>Correct Answer:</strong> It is absorbed shortly after birth.</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 10</h3>
                <p><strong>If a baby is born prematurely before type II cells produce sufficient pulmonary surfactant, which of the following might you expect?</strong></p>
                <ul>
                  <li>no difficulty as type III cells can provide enough surfactant for normal breathing</li>
                  <li>difficulty with pulmonary capillary flow</li>
                  <li>difficulty expressing fluid</li>
                  <li>difficulty inflating the lungs</li>
                </ul>
                <p><strong>Correct Answer:</strong> difficulty inflating the lungs</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 11</h3>
                <p><strong>Contraction of the external intercostal muscles causes which of the following to occur?</strong></p>
                <ul>
                  <li>The diaphragm moves downward.</li>
                  <li>The ribs and sternum move upward.</li>
                  <li>The rib cage is compressed.</li>
                  <li>The thoracic cavity volume decreases.</li>
                </ul>
                <p><strong>Correct Answer:</strong> The ribs and sternum move upward.</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 12</h3>
                <p><strong>Exercise can trigger symptoms of AMS due to which of the following?</strong></p>
                <ul>
                  <li>abnormal neural signals</li>
                  <li>small venous reserve of oxygen</li>
                  <li>low partial pressure of oxygen</li>
                  <li>low atmospheric pressure</li>
                </ul>
                <p><strong>Correct Answer:</strong> small venous reserve of oxygen</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 13</h3>
                <p><strong>Which of the following prevents the alveoli from collapsing?</strong></p>
                <ul>
                  <li>expiratory reserve volume</li>
                  <li>residual volume</li>
                  <li>tidal volume</li>
                  <li>inspiratory reserve volume</li>
                </ul>
                <p><strong>Correct Answer:</strong> residual volume</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 14</h3>
                <p><strong>Gas exchange that occurs at the level of the tissues is called ________.</strong></p>
                <ul>
                  <li>external respiration</li>
                  <li>interpulmonary respiration</li>
                  <li>internal respiration</li>
                  <li>pulmonary ventilation</li>
                </ul>
                <p><strong>Correct Answer:</strong> internal respiration</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 15</h3>
                <p><strong>Oxyhemoglobin forms by a chemical reaction between which of the following?</strong></p>
                <ul>
                  <li>carbonic anhydrase and carbon dioxide</li>
                  <li>carbonic anhydrase and oxygen</li>
                  <li>hemoglobin and oxygen</li>
                  <li>hemoglobin and carbon dioxide</li>
                </ul>
                <p><strong>Correct Answer:</strong> hemoglobin and oxygen</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 16</h3>
                <p><strong>Which of the following occurs during the chloride shift?</strong></p>
                <ul>
                  <li>Bicarbonate is removed from the erythrocyte.</li>
                  <li>Chloride is exchanged for bicarbonate.</li>
                  <li>Bicarbonate is removed from the blood.</li>
                  <li>Chloride is removed from the erythrocyte.</li>
                </ul>
                <p><strong>Correct Answer:</strong> Chloride is exchanged for bicarbonate.</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 17</h3>
                <p><strong>Which of the following processes does atmospheric pressure play a role in?</strong></p>
                <ul>
                  <li>production of pulmonary surfactant</li>
                  <li>pulmonary ventilation</li>
                  <li>surface tension</li>
                  <li>resistance</li>
                </ul>
                <p><strong>Correct Answer:</strong> pulmonary ventilation</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 18</h3>
                <p><strong>A low partial pressure of oxygen promotes hemoglobin binding to carbon dioxide. This is an example of the ________.</strong></p>
                <ul>
                  <li>Henry’s law</li>
                  <li>Dalton’s law</li>
                  <li>Haldane effect</li>
                  <li>Bohr effect</li>
                </ul>
                <p><strong>Correct Answer:</strong> Haldane effect</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 19</h3>
                <p><strong>Increased ventilation that results in an increase in blood pH is called ________.</strong></p>
                <ul>
                  <li>hyperpnea</li>
                  <li>acclimatization</li>
                  <li>apnea</li>
                  <li>hyperventilation</li>
                </ul>
                <p><strong>Correct Answer:</strong> hyperventilation</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 20</h3>
                <p><strong>The ________________________ is a tube connected to the trachea that branches into many subsidiaries and provides a passageway for air to enter and leave the lungs.</strong></p>
                <ul>
                  <li>illiac</li>
                  <li>trachea</li>
                  <li>bronchus</li>
                  <li>aorta</li>
                </ul>
                <p><strong>Correct Answer:</strong> bronchus</p>
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
                <p><strong>The kidneys are situated more posterior (towards the back) than anterior.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Kidneys filter blood and release urine.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>Arteries contain no waste products.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>There is much more oxygen in venous blood.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>Capillaries connect the arteries to the veins to help move blood across the kidneys.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 25 - Quiz</h3>
			<article>
                <h3>Question 1</h3>
                <p><strong>What are the functional units of the kidney that carry out all filtration and modification to produce urine?</strong></p>
                <ul>
                  <li>pedicles</li>
                  <li>nephrons</li>
                  <li>neurons</li>
                  <li>oliguria</li>
                </ul>
                <p><strong>Correct Answer:</strong> nephrons</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>Which part of the urinary system is not completely retroperitoneal?</strong></p>
                <ul>
                  <li>kidneys</li>
                  <li>nephrons</li>
                  <li>ureters</li>
                  <li>bladder</li>
                </ul>
                <p><strong>Correct Answer:</strong> bladder</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>Which step in vitamin D production does the kidney perform?</strong></p>
                <ul>
                  <li>stores vitamin A</li>
                  <li>converts cholecalciferol into calcidiol</li>
                  <li>all of these</li>
                  <li>converts calcidiol into calcitriol</li>
                </ul>
                <p><strong>Correct Answer:</strong> converts calcidiol into calcitriol</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>The renal pyramids are separated from each other by extensions of the renal cortex called ________.</strong></p>
                <ul>
                  <li>medullary cortices</li>
                  <li>minor calyces</li>
                  <li>renal columns</li>
                  <li>renal medulla</li>
                </ul>
                <p><strong>Correct Answer:</strong> renal columns</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>________________________ is a protein-forming water channels through the lipid bilayer of the cell and allows water to cross.</strong></p>
                <ul>
                  <li>Glycosuria</li>
                  <li>Aquaporin</li>
                  <li>Anuria</li>
                  <li>Medulla</li>
                </ul>
                <p><strong>Correct Answer:</strong> Aquaporin</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 6</h3>
                <p><strong>If there were no aquaporin channels in the collecting duct, ________________________.</strong></p>
                <ul>
                  <li>you would retain excess Na+</li>
                  <li>you would suffer severe dehydration</li>
                  <li>you would develop systemic edema</li>
                  <li>you would lose vitamins and electrolytes</li>
                </ul>
                <p><strong>Correct Answer:</strong> you would suffer severe dehydration</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 7</h3>
                <p><strong>The primary structure found within the medulla is the ________.</strong></p>
                <ul>
                  <li>minor calyces</li>
                  <li>ureter</li>
                  <li>loop of Henle</li>
                  <li>portal system</li>
                </ul>
                <p><strong>Correct Answer:</strong> loop of Henle</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 8</h3>
                <p><strong>Which of these beverages does not have a diuretic effect?</strong></p>
                <ul>
                  <li>alcohol</li>
                  <li>coffee</li>
                  <li>milk</li>
                  <li>tea</li>
                </ul>
                <p><strong>Correct Answer:</strong> milk</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 9</h3>
                <p><strong>Which hormone does the kidney produce that stimulates red blood cell production?</strong></p>
                <ul>
                  <li>thrombopoietin</li>
                  <li>renin</li>
                  <li>EPO</li>
                  <li>vitamin D</li>
                </ul>
                <p><strong>Correct Answer:</strong> EPO</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 10</h3>
                <p><strong>The right kidney is slightly lower because ________.</strong></p>
                <ul>
                  <li>it is displace by the heart</li>
                  <li>it is slightly smaller</li>
                  <li>it is displaced by the liver</li>
                  <li>it needs protection of the lower ribs</li>
                </ul>
                <p><strong>Correct Answer:</strong> it is displaced by the liver</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 11</h3>
                <p><strong>Peristaltic contractions occur in the ________.</strong></p>
                <ul>
                  <li>ureters</li>
                  <li>bladder</li>
                  <li>urethra</li>
                  <li>urethra, bladder, and ureters</li>
                </ul>
                <p><strong>Correct Answer:</strong> ureters</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 12</h3>
                <p><strong>Which of these is a vasoconstrictor?</strong></p>
                <ul>
                  <li>natriuretic hormone</li>
                  <li>angiotensin II</li>
                  <li>nitric oxide</li>
                  <li>bradykinin</li>
                </ul>
                <p><strong>Correct Answer:</strong> angiotensin II</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 13</h3>
                <p><strong>What are the names of the capillaries following the efferent arteriole?</strong></p>
                <ul>
                  <li>interlobar and interlobular</li>
                  <li>arcuate and medullary</li>
                  <li>peritubular and medullary</li>
                  <li>peritubular and vasa recta</li>
                </ul>
                <p><strong>Correct Answer:</strong> peritubular and vasa recta</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 14</h3>
                <p><strong>The functional unit of the kidney is called _______ .</strong></p>
                <ul>
                  <li>Bowman’s capsule</li>
                  <li>the renal hilus</li>
                  <li>the renal corpuscle</li>
                  <li>the nephron</li>
                </ul>
                <p><strong>Correct Answer:</strong> the nephron</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 15</h3>
                <p><strong>Production of urine to modify plasma makeup is the result of ________.</strong></p>
                <ul>
                  <li>secretion</li>
                  <li>filtration</li>
                  <li>filtration, absorption, and secretion</li>
                  <li>absorption</li>
                </ul>
                <p><strong>Correct Answer:</strong> filtration, absorption, and secretion</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 16</h3>
                <p><strong>The fine tuning of water recovery or disposal occurs in ________.</strong></p>
                <ul>
                  <li>the ascending loop of Henle</li>
                  <li>the collecting ducts</li>
                  <li>the proximal convoluted tubule</li>
                  <li>the distal convoluted tubule</li>
                </ul>
                <p><strong>Correct Answer:</strong> the collecting ducts</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 17</h3>
                <p><strong>Blood filtrate is captured in the lumen of the ________.</strong></p>
                <ul>
                  <li>glomerulus</li>
                  <li>calyces</li>
                  <li>Bowman’s capsule</li>
                  <li>renal papillae</li>
                </ul>
                <p><strong>Correct Answer:</strong> Bowman’s capsule</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 18</h3>
                <p><strong>Which of these three paracrine chemicals cause vasodilation?</strong></p>
                <ul>
                  <li>hydrogen peroxide</li>
                  <li>adenosine</li>
                  <li>nitric oxide</li>
                  <li>ATP</li>
                </ul>
                <p><strong>Correct Answer:</strong> nitric oxide</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 19</h3>
                <p><strong>What hormone directly opposes the actions of natriuretic hormones?</strong></p>
                <ul>
                  <li>renin</li>
                  <li>nitric oxide</li>
                  <li>aldosterone</li>
                  <li>dopamine</li>
                </ul>
                <p><strong>Correct Answer:</strong> aldosterone</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 20</h3>
                <p><strong>What signal causes the heart to secrete atrial natriuretic hormone?</strong></p>
                <ul>
                  <li>decreased blood pressure</li>
                  <li>increased Na+ levels</li>
                  <li>decreased Na+ levels</li>
                  <li>increased blood pressure</li>
                </ul>
                <p><strong>Correct Answer:</strong> increased blood pressure</p>
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
                <p><strong>During a vasectomy, a small incision is made into the scrotum.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>During a vasectomy, the vas deferens is then severed to prevent sperm from travelling.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>LH is a hormone created by the pituitary gland.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>LH is not involved in the release of the egg.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> False</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>Once in the fallopian tube, an egg will either become fertilized by a sperm or dissolved if not fertilized.</strong></p>
                <ul>
                  <li>True</li>
                  <li>False</li>
                </ul>
                <p><strong>Correct Answer:</strong> True</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<h3>Chapter 27 - Quiz</h3>
			<article>
                <h3>Question 1</h3>
                <p><strong>Spermatogenesis takes place in the ________.</strong></p>
                <ul>
                  <li>prostate gland</li>
                  <li>ejaculatory duct</li>
                  <li>glans penis</li>
                  <li>seminiferous tubules</li>
                </ul>
                <p><strong>Correct Answer:</strong> seminiferous tubules</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 2</h3>
                <p><strong>The _______________ is a fluid-filled chamber that characterizes a mature tertiary follicle.</strong></p>
                <ul>
                  <li>cervix</li>
                  <li>antrum</li>
                  <li>ductus</li>
                  <li>atrium</li>
                </ul>
                <p><strong>Correct Answer:</strong> antrum</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 3</h3>
                <p><strong>What are the female gonads called?</strong></p>
                <ul>
                  <li>oocytes</li>
                  <li>ovaries</li>
                  <li>ova</li>
                  <li>oviducts</li>
                </ul>
                <p><strong>Correct Answer:</strong> ovaries</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 4</h3>
                <p><strong>From what structure does the corpus luteum originate?</strong></p>
                <ul>
                  <li>uterine corpus</li>
                  <li>fallopian tube</li>
                  <li>corpus albicans</li>
                  <li>dominant follicle</li>
                </ul>
                <p><strong>Correct Answer:</strong> dominant follicle</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 5</h3>
                <p><strong>What is the function of the epididymis?</strong></p>
                <ul>
                  <li>sperm maturation and storage</li>
                  <li>produces the bulk of seminal fluid</li>
                  <li>provides nitric oxide needed for erections</li>
                  <li>spermatogenesis</li>
                </ul>
                <p><strong>Correct Answer:</strong> sperm maturation and storage</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 6</h3>
                <p><strong>Leydig cells ________.</strong></p>
                <ul>
                  <li>secrete seminal fluid</li>
                  <li>secrete testosterone</li>
                  <li>support spermatogenesis</li>
                  <li>activate the sperm flagellum</li>
                </ul>
                <p><strong>Correct Answer:</strong> secrete testosterone</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 7</h3>
                <p><strong>Where does fertilization of the egg by the sperm typically occur?</strong></p>
                <ul>
                  <li>ovary</li>
                  <li>vagina</li>
                  <li>uterine tube</li>
                  <li>uterus</li>
                </ul>
                <p><strong>Correct Answer:</strong> uterine tube</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 8</h3>
                <p><strong>Spermatogenesis begins with mitotic division of spermatogonia (stem cells) to produce primary spermatocytes that undergo Meiosis I to create ____ secondary spermatocytes.</strong></p>
                <ul>
                  <li>1</li>
                  <li>2</li>
                  <li>4</li>
                  <li>3</li>
                </ul>
                <p><strong>Correct Answer:</strong> 2</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 9</h3>
                <p><strong>The ___________________ glands are glands that secrete a lubricating mucus that cleans and lubricates the urethra prior to and during ejaculation.</strong></p>
                <ul>
                  <li>bulbourethral</li>
                  <li>corpus</li>
                  <li>ductus</li>
                  <li>urinary</li>
                </ul>
                <p><strong>Correct Answer:</strong> bulbourethral</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 10</h3>
                <p><strong>Which hypothalamic hormone contributes to the regulation of the male reproductive system?</strong></p>
                <ul>
                  <li>follicle-stimulating hormone</li>
                  <li>gonadotropin-releasing hormone</li>
                  <li>androgens</li>
                  <li>luteinizing hormone</li>
                </ul>
                <p><strong>Correct Answer:</strong> gonadotropin-releasing hormone</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 11</h3>
                <p><strong>Why do estrogen levels fall after menopause?</strong></p>
                <ul>
                  <li>The pituitary secretes a menopause-specific hormone.</li>
                  <li>The ovaries degrade.</li>
                  <li>The cells of the endometrium degenerate.</li>
                  <li>There are no follicles left to produce estrogen.</li>
                </ul>
                <p><strong>Correct Answer:</strong> There are no follicles left to produce estrogen.</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 12</h3>
                <p><strong>When do the oogonia undergo mitosis?</strong></p>
                <ul>
                  <li>before birth</li>
                  <li>during fertilization</li>
                  <li>at puberty</li>
                  <li>at the beginning of each menstrual cycle</li>
                </ul>
                <p><strong>Correct Answer:</strong> before birth</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 13</h3>
                <p><strong>The vulva includes the ________.</strong></p>
                <ul>
                  <li>lactiferous duct, rugae, and hymen</li>
                  <li>lactiferous duct, endometrium, and bulbourethral glands</li>
                  <li>mons pubis, labia majora, and Bartholin’s glands</li>
                  <li>mons pubis, endometrium, and hymen</li>
                </ul>
                <p><strong>Correct Answer:</strong> mons pubis, labia majora, and Bartholin’s glands</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 14</h3>
                <p><strong>The ____________________ are fingerlike projections on the distal uterine tubes.</strong></p>
                <ul>
                  <li>epididymis</li>
                  <li>follicle</li>
                  <li>isthmus</li>
                  <li>fimbriae</li>
                </ul>
                <p><strong>Correct Answer:</strong> fimbriae</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 15</h3>
                <p><strong>What controls whether an embryo will develop testes or ovaries?</strong></p>
                <ul>
                  <li>presence or absence of estrogen</li>
                  <li>Y chromosome</li>
                  <li>pituitary gland</li>
                  <li>hypothalamus</li>
                </ul>
                <p><strong>Correct Answer:</strong> Y chromosome</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 16</h3>
                <p><strong>What are male gametes called?</strong></p>
                <ul>
                  <li>testosterone</li>
                  <li>testes</li>
                  <li>sperm</li>
                  <li>ova</li>
                </ul>
                <p><strong>Correct Answer:</strong> sperm</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 17</h3>
                <p><strong>Without SRY expression, an embryo will develop ________.</strong></p>
                <ul>
                  <li>male reproductive structures 50 percent of the time and female reproductive structures 50 percent of the time</li>
                  <li>no reproductive structures</li>
                  <li>female reproductive structures</li>
                  <li>male reproductive structures</li>
                </ul>
                <p><strong>Correct Answer:</strong> female reproductive structures</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 18</h3>
                <p><strong>The timing of puberty can be influenced by which of the following?</strong></p>
                <ul>
                  <li>stress</li>
                  <li>genes</li>
                  <li>all of these</li>
                  <li>amount of body fat</li>
                </ul>
                <p><strong>Correct Answer:</strong> all of these</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 19</h3>
                <p><strong>What is a gamete?</strong></p>
                <ul>
                  <li>a diploid somatic cell that contributes genetic material to form an offspring</li>
                  <li>a haploid reproductive cell that contributes genetic material to form an offspring</li>
                  <li>a haploid somatic cell that contributes genetic material to form an offspring</li>
                  <li>a diploid reproductive cell that contributes genetic material to form an offspring</li>
                </ul>
                <p><strong>Correct Answer:</strong> a haploid reproductive cell that contributes genetic material to form an offspring</p>
                <p><strong>Explanation:</strong></p>
			</article>

			<article>
                <h3>Question 20</h3>
                <p><strong>Which term describes the lactiferous sinus area of milk collection between alveoli and lactiferous duct?</strong></p>
                <ul>
                  <li>mammary glands</li>
                  <li>lactiferous ducts</li>
                  <li>lactiferous sinus</li>
                  <li>Leydig cells</li>
                </ul>
                <p><strong>Correct Answer:</strong> lactiferous sinus</p>
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
				<p><strong>Fertilization occurs when the sperm and egg fuse.</strong></p>
				<ul>
					<li>True</li>
					<li>False</li>
				</ul>
				<p><strong>Correct Answer:</strong> True</p>
				<p><strong>Explanation:</strong> Fertilization is the process where the sperm and egg fuse to form a zygote, marking the beginning of a new organism.</p>
			</article>

			<article>
				<h3>Question 2</h3>
				<p><strong>Egg cells are much smaller than sperm cells.</strong></p>
				<ul>
					<li>True</li>
					<li>False</li>
				</ul>
				<p><strong>Correct Answer:</strong> False</p>
				<p><strong>Explanation:</strong> Egg cells are much larger than sperm cells, as they contain nutrients and organelles necessary for early development.</p>
			</article>

			<article>
				<h3>Question 3</h3>
				<p><strong>Sex cells are also known as gametes.</strong></p>
				<ul>
					<li>True</li>
					<li>False</li>
				</ul>
				<p><strong>Correct Answer:</strong> True</p>
				<p><strong>Explanation:</strong> Gametes are the reproductive cells (sperm and egg) that carry half the genetic material of an organism.</p>
			</article>

			<article>
				<h3>Question 4</h3>
				<p><strong>Each egg and each sperm contain 23 chromosomes (not 23 pairs of chromosomes).</strong></p>
				<ul>
					<li>True</li>
					<li>False</li>
				</ul>
				<p><strong>Correct Answer:</strong> True</p>
				<p><strong>Explanation:</strong> Gametes are haploid cells, meaning they contain 23 chromosomes, which combine during fertilization to form a diploid zygote.</p>
			</article>

			<article>
				<h3>Question 5</h3>
				<p><strong>A blastocyst is a fertilized egg that is about 5-9 days old.</strong></p>
				<ul>
					<li>True</li>
					<li>False</li>
				</ul>
				<p><strong>Correct Answer:</strong> True</p>
				<p><strong>Explanation:</strong> A blastocyst is a structure formed in the early development of mammals, consisting of a hollow ball of cells.</p>
			</article>

			<article>
				<h3>Question 17</h3>
				<p><strong>During weeks 9–12 of fetal development, ________.</strong></p>
				<ul>
					<li>Surfactant production begins in the fetal lungs</li>
					<li>The spinal cord begins to be myelinated</li>
					<li>Meconium begins to accumulate in the intestines</li>
					<li>Bone marrow begins to assume erythrocyte production</li>
				</ul>
				<p><strong>Correct Answer:</strong> Bone marrow begins to assume erythrocyte production</p>
				<p><strong>Explanation:</strong> During this period, the bone marrow starts producing red blood cells, a critical step in fetal development.</p>
			</article>

			<article>
				<h3>Question 18</h3>
				<p><strong>The placenta is formed from ________.</strong></p>
				<ul>
					<li>The mother’s endometrium only</li>
					<li>The embryo’s mesenchymal cells</li>
					<li>The mother’s endometrium and the embryo’s chorionic membrane</li>
					<li>The mother’s endometrium and the embryo’s umbilical cord</li>
				</ul>
				<p><strong>Correct Answer:</strong> The mother’s endometrium and the embryo’s chorionic membrane</p>
				<p><strong>Explanation:</strong> The placenta is a structure that develops from both maternal and embryonic tissues to support the fetus.</p>
			</article>

			<article>
				<h3>Question 19</h3>
				<p><strong>Which of the following is a possible culprit of “morning sickness”?</strong></p>
				<ul>
					<li>Increased minute respiration</li>
					<li>Increased blood volume</li>
					<li>Decreased intestinal peristalsis</li>
					<li>Decreased aldosterone secretion</li>
				</ul>
				<p><strong>Correct Answer:</strong> Decreased intestinal peristalsis</p>
				<p><strong>Explanation:</strong> Hormonal changes during pregnancy can slow down intestinal movement, leading to nausea and vomiting.</p>
			</article>

			<article>
				<h3>Question 20</h3>
				<p><strong>How does the decrease in progesterone at the last weeks of pregnancy help to bring on labor?</strong></p>
				<ul>
					<li>Stimulating FSH production</li>
					<li>Decreasing the inhibition of uterine contractility</li>
					<li>Decreasing the levels of estrogens</li>
					<li>Dilating the cervix</li>
				</ul>
				<p><strong>Correct Answer:</strong> Decreasing the inhibition of uterine contractility</p>
				<p><strong>Explanation:</strong> Lower progesterone levels reduce the suppression of uterine contractions, facilitating the onset of labor.</p>
			</article>
		</div>
	</section>
</main>